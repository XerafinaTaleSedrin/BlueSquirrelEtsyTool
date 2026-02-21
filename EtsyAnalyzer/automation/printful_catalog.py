#!/usr/bin/env python3
"""
Printful Product Catalog Management System
Handles downloading, parsing, and validating Printful's complete product catalog
"""

import requests
import csv
import json
import sqlite3
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PrintfulCatalogManager:
    """Manages Printful product catalog with automatic updates and validation"""

    def __init__(self, database_path: str = "workflow_state.db", catalog_dir: str = "DESIGNS/printful_catalog"):
        self.database_path = database_path
        self.catalog_dir = Path(catalog_dir)
        self.catalog_dir.mkdir(parents=True, exist_ok=True)
        self.csv_file_path = self.catalog_dir / "printful_products.csv"
        self.last_update_file = self.catalog_dir / "last_update.json"

        # Printful product catalog URLs
        self.catalog_urls = {
            'products_csv': 'https://www.printful.com/api/v1/store/products.csv',
            'api_products': 'https://api.printful.com/products'
        }

        self._initialize_database()

    def _initialize_database(self):
        """Initialize database tables for catalog management"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        # Printful products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS printful_products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER UNIQUE NOT NULL,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                type_name TEXT NOT NULL,
                brand TEXT,
                model TEXT,
                image TEXT,
                variant_count INTEGER DEFAULT 0,
                is_discontinued BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Printful variants table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS printful_variants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                variant_id INTEGER UNIQUE NOT NULL,
                product_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                size TEXT,
                color TEXT,
                color_code TEXT,
                image TEXT,
                price REAL,
                in_stock BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES printful_products (product_id)
            )
        ''')

        # Catalog update history table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS catalog_updates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                update_type TEXT NOT NULL,
                status TEXT NOT NULL,
                products_added INTEGER DEFAULT 0,
                products_removed INTEGER DEFAULT 0,
                products_updated INTEGER DEFAULT 0,
                error_message TEXT,
                update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()

    def download_catalog(self, force_update: bool = False) -> Dict:
        """Download the latest Printful catalog"""
        try:
            # Check if update is needed
            if not force_update and self._is_catalog_current():
                return {
                    'success': True,
                    'message': 'Catalog is current, no update needed',
                    'last_update': self.get_last_update_info()
                }

            logger.info("Downloading Printful product catalog...")

            # Try API first (more comprehensive data)
            try:
                api_data = self._download_from_api()
                if api_data:
                    result = self._process_api_data(api_data)
                    self._record_update('api', 'success', result)
                    return {
                        'success': True,
                        'message': f'Catalog updated via API: {result["products_added"]} products',
                        'data': result
                    }
            except Exception as e:
                logger.warning(f"API download failed: {e}, trying CSV fallback...")

            # Fallback to CSV download
            csv_data = self._download_csv()
            if csv_data:
                result = self._process_csv_data(csv_data)
                self._record_update('csv', 'success', result)
                return {
                    'success': True,
                    'message': f'Catalog updated via CSV: {result["products_added"]} products',
                    'data': result
                }

            raise Exception("Both API and CSV download methods failed")

        except Exception as e:
            error_msg = f"Catalog download failed: {str(e)}"
            logger.error(error_msg)
            self._record_update('failed', 'error', {'error_message': error_msg})
            return {'success': False, 'error': error_msg}

    def _download_from_api(self) -> Optional[Dict]:
        """Download catalog data from Printful API"""
        try:
            response = requests.get(self.catalog_urls['api_products'], timeout=30)
            response.raise_for_status()

            data = response.json()
            if data.get('code') == 200 and 'result' in data:
                logger.info(f"Successfully downloaded {len(data['result'])} products from API")
                return data['result']

            return None
        except Exception as e:
            logger.error(f"API download error: {e}")
            return None

    def _download_csv(self) -> Optional[List[Dict]]:
        """Download catalog data from CSV"""
        try:
            # Note: The actual CSV URL might need authentication or be different
            # This is a placeholder - you may need to manually download the CSV
            # from Printful dashboard and place it in the catalog directory

            if self.csv_file_path.exists():
                logger.info("Using existing CSV file")
                with open(self.csv_file_path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    return list(reader)

            # Try downloading if URL is available
            response = requests.get(self.catalog_urls['products_csv'], timeout=30)
            response.raise_for_status()

            # Save CSV file
            with open(self.csv_file_path, 'w', encoding='utf-8') as f:
                f.write(response.text)

            # Parse CSV
            with open(self.csv_file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)
                logger.info(f"Successfully downloaded CSV with {len(data)} entries")
                return data

        except Exception as e:
            logger.error(f"CSV download error: {e}")
            return None

    def _process_api_data(self, products: List[Dict]) -> Dict:
        """Process product data from API"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        products_added = 0
        products_updated = 0

        try:
            for product in products:
                product_id = product.get('id')
                if not product_id:
                    continue

                # Check if product exists
                cursor.execute('SELECT id FROM printful_products WHERE product_id = ?', (product_id,))
                existing = cursor.fetchone()

                product_data = (
                    product_id,
                    product.get('title', ''),
                    product.get('type', ''),
                    product.get('type_name', ''),
                    product.get('brand', ''),
                    product.get('model', ''),
                    product.get('image', ''),
                    len(product.get('variants', [])),
                    0,  # is_discontinued
                    datetime.now().isoformat()
                )

                if existing:
                    cursor.execute('''
                        UPDATE printful_products
                        SET name=?, type=?, type_name=?, brand=?, model=?,
                            image=?, variant_count=?, updated_at=?
                        WHERE product_id=?
                    ''', product_data[1:] + (product_id,))
                    products_updated += 1
                else:
                    cursor.execute('''
                        INSERT INTO printful_products
                        (product_id, name, type, type_name, brand, model, image, variant_count, is_discontinued, updated_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', product_data)
                    products_added += 1

                # Process variants
                self._process_variants(cursor, product_id, product.get('variants', []))

            conn.commit()

            # Update last update timestamp
            self._save_update_info()

            return {
                'products_added': products_added,
                'products_updated': products_updated,
                'total_products': len(products)
            }

        finally:
            conn.close()

    def _process_csv_data(self, csv_data: List[Dict]) -> Dict:
        """Process product data from CSV"""
        # CSV processing logic would depend on the actual CSV format
        # This is a placeholder implementation
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        products_added = 0

        try:
            for row in csv_data:
                # Adapt field names based on actual CSV structure
                product_id = row.get('product_id') or row.get('id')
                if not product_id:
                    continue

                cursor.execute('SELECT id FROM printful_products WHERE product_id = ?', (product_id,))
                if not cursor.fetchone():
                    cursor.execute('''
                        INSERT OR IGNORE INTO printful_products
                        (product_id, name, type, type_name, updated_at)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (
                        product_id,
                        row.get('name', ''),
                        row.get('type', ''),
                        row.get('type_name', ''),
                        datetime.now().isoformat()
                    ))
                    products_added += 1

            conn.commit()
            self._save_update_info()

            return {
                'products_added': products_added,
                'products_updated': 0,
                'total_products': len(csv_data)
            }

        finally:
            conn.close()

    def _process_variants(self, cursor, product_id: int, variants: List[Dict]):
        """Process product variants"""
        for variant in variants:
            variant_id = variant.get('id')
            if not variant_id:
                continue

            cursor.execute('SELECT id FROM printful_variants WHERE variant_id = ?', (variant_id,))
            if not cursor.fetchone():
                cursor.execute('''
                    INSERT OR IGNORE INTO printful_variants
                    (variant_id, product_id, name, size, color, color_code, image, price, in_stock)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    variant_id,
                    product_id,
                    variant.get('name', ''),
                    variant.get('size', ''),
                    variant.get('color', ''),
                    variant.get('color_code', ''),
                    variant.get('image', ''),
                    variant.get('price', 0),
                    variant.get('availability_status', '') == 'active'
                ))

    def _is_catalog_current(self, days_threshold: int = 30) -> bool:
        """Check if catalog was updated within threshold"""
        update_info = self.get_last_update_info()
        if not update_info:
            return False

        last_update = datetime.fromisoformat(update_info['timestamp'])
        threshold_date = datetime.now() - timedelta(days=days_threshold)

        return last_update > threshold_date

    def _save_update_info(self):
        """Save update timestamp"""
        update_info = {
            'timestamp': datetime.now().isoformat(),
            'version': '1.0'
        }

        with open(self.last_update_file, 'w') as f:
            json.dump(update_info, f, indent=2)

    def _record_update(self, update_type: str, status: str, result: Dict):
        """Record update in database"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO catalog_updates
            (update_type, status, products_added, products_removed, products_updated, error_message)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            update_type,
            status,
            result.get('products_added', 0),
            result.get('products_removed', 0),
            result.get('products_updated', 0),
            result.get('error_message', '')
        ))

        conn.commit()
        conn.close()

    def get_last_update_info(self) -> Optional[Dict]:
        """Get last update information"""
        if self.last_update_file.exists():
            try:
                with open(self.last_update_file, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        return None

    def get_catalog_status(self) -> Dict:
        """Get current catalog status for dashboard"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        # Get product counts
        cursor.execute('SELECT COUNT(*) FROM printful_products WHERE is_discontinued = 0')
        active_products = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM printful_variants WHERE in_stock = 1')
        active_variants = cursor.fetchone()[0]

        # Get last update
        cursor.execute('''
            SELECT update_timestamp, status, products_added, products_updated
            FROM catalog_updates
            ORDER BY update_timestamp DESC
            LIMIT 1
        ''')
        last_update = cursor.fetchone()

        conn.close()

        # Determine status
        update_info = self.get_last_update_info()
        status = 'unknown'
        days_old = None

        if update_info:
            last_update_date = datetime.fromisoformat(update_info['timestamp'])
            days_old = (datetime.now() - last_update_date).days

            if days_old <= 30:
                status = 'current'
            elif days_old <= 45:
                status = 'needs_update'
            else:
                status = 'outdated'

        return {
            'status': status,
            'active_products': active_products,
            'active_variants': active_variants,
            'last_update': update_info,
            'days_old': days_old,
            'last_update_record': last_update
        }

    def validate_products(self, product_names: List[str]) -> Dict:
        """Validate if products exist in Printful catalog"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        valid_products = []
        invalid_products = []
        suggestions = {}

        for product_name in product_names:
            # Exact match
            cursor.execute('''
                SELECT name, type_name FROM printful_products
                WHERE LOWER(name) LIKE LOWER(?) AND is_discontinued = 0
            ''', (f'%{product_name}%',))

            matches = cursor.fetchall()

            if matches:
                valid_products.append({
                    'requested': product_name,
                    'matches': [{'name': m[0], 'type': m[1]} for m in matches]
                })
            else:
                invalid_products.append(product_name)

                # Find similar products
                cursor.execute('''
                    SELECT name, type_name FROM printful_products
                    WHERE is_discontinued = 0
                    ORDER BY name
                    LIMIT 5
                ''')
                similar = cursor.fetchall()
                suggestions[product_name] = [{'name': s[0], 'type': s[1]} for s in similar]

        conn.close()

        return {
            'valid_products': valid_products,
            'invalid_products': invalid_products,
            'suggestions': suggestions
        }

    def get_products_by_category(self, category: str = None) -> List[Dict]:
        """Get products filtered by category"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        if category:
            cursor.execute('''
                SELECT product_id, name, type, type_name, brand, variant_count
                FROM printful_products
                WHERE type_name LIKE ? AND is_discontinued = 0
                ORDER BY name
            ''', (f'%{category}%',))
        else:
            cursor.execute('''
                SELECT product_id, name, type, type_name, brand, variant_count
                FROM printful_products
                WHERE is_discontinued = 0
                ORDER BY type_name, name
            ''')

        products = []
        for row in cursor.fetchall():
            products.append({
                'product_id': row[0],
                'name': row[1],
                'type': row[2],
                'type_name': row[3],
                'brand': row[4],
                'variant_count': row[5]
            })

        conn.close()
        return products


# Convenience functions for integration
def get_catalog_manager() -> PrintfulCatalogManager:
    """Get singleton catalog manager instance"""
    return PrintfulCatalogManager()


def validate_printful_products(product_names: List[str]) -> Dict:
    """Quick validation function for use in other modules"""
    manager = get_catalog_manager()
    return manager.validate_products(product_names)


def get_available_products(category: str = None) -> List[Dict]:
    """Get available Printful products"""
    manager = get_catalog_manager()
    return manager.get_products_by_category(category)


if __name__ == "__main__":
    # Test the catalog manager
    manager = PrintfulCatalogManager()

    print("Downloading Printful catalog...")
    result = manager.download_catalog(force_update=True)
    print(f"Result: {result}")

    print("\nCatalog status:")
    status = manager.get_catalog_status()
    print(f"Status: {status}")

    print("\nTesting product validation:")
    test_products = ['t-shirt', 'hoodie', 'lanyard', 'mug']
    validation = manager.validate_products(test_products)
    print(f"Validation: {validation}")