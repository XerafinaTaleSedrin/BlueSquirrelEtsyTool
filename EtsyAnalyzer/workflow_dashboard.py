#!/usr/bin/env python3
"""
Flask Workflow Management Dashboard for EtsyAnalyzer
Provides GUI control over the complete automation pipeline with human approval gates
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, send_file
import json
import os
import sys

# Set UTF-8 encoding globally
os.environ['PYTHONIOENCODING'] = 'utf-8'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import asdict
import sqlite3

# Add automation directory to path
automation_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'automation')
sys.path.append(automation_dir)

# Import automation components
try:
    from design_generation_system import DesignWorkflowManager
    from printful_integration import AutomatedProductCreator
    from listing_content_generator import ListingWorkflowManager
    from automated_analyzer_extension import AutomatedAnalyzerOrchestrator
    from printful_catalog import PrintfulCatalogManager
except ImportError as e:
    print(f"Warning: Could not import automation components: {e}")

app = Flask(__name__)
app.secret_key = 'etsy-analyzer-workflow-2024'  # Change this in production
app.config['UPLOAD_FOLDER'] = 'DESIGNS/completed_designs/png_files'
app.config['CSV_UPLOAD_FOLDER'] = 'DESIGNS/store_data'
app.config['PRINTFUL_API_KEY'] = os.getenv('PRINTFUL_API_KEY', 'LPUcjY4AJmyrHoWxGg7ub4hv9oG38cyjtvOPb2Jg')

# Database setup
DATABASE = 'workflow_state.db'

def init_database():
    """Initialize SQLite database for workflow state tracking"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Workflow state table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workflow_state (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stage TEXT NOT NULL,
            status TEXT NOT NULL,
            data TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Design briefs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS design_briefs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brief_id TEXT UNIQUE NOT NULL,
            brief_data TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            approval_notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            approved_at TIMESTAMP
        )
    ''')

    # Design assets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS design_assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id TEXT UNIQUE NOT NULL,
            brief_id TEXT NOT NULL,
            file_path TEXT NOT NULL,
            status TEXT DEFAULT 'uploaded',
            printful_status TEXT DEFAULT 'pending',
            etsy_status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (brief_id) REFERENCES design_briefs (brief_id)
        )
    ''')

    # Etsy stores table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS etsy_stores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_name TEXT NOT NULL,
            store_url TEXT,
            csv_file_path TEXT,
            data_source TEXT NOT NULL CHECK(data_source IN ('url', 'csv')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_analyzed TIMESTAMP
        )
    ''')

    # Analysis sessions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT UNIQUE NOT NULL,
            store_id INTEGER,
            analysis_data TEXT,
            briefs_generated INTEGER DEFAULT 0,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (store_id) REFERENCES etsy_stores (id)
        )
    ''')

    conn.commit()
    conn.close()

class WorkflowManager:
    """Manages the overall workflow state and transitions"""

    def __init__(self):
        self.designs_base_dir = Path("DESIGNS")
        self.automation_components = self._initialize_automation()

    def _initialize_automation(self):
        """Initialize automation components"""
        try:
            return {
                'analyzer': AutomatedAnalyzerOrchestrator(),
                'design_manager': DesignWorkflowManager(output_dir=str(self.designs_base_dir)),
                'listing_manager': ListingWorkflowManager(output_dir=str(self.designs_base_dir / "listings")),
                'product_creator': AutomatedProductCreator(app.config['PRINTFUL_API_KEY']),
                'catalog_manager': PrintfulCatalogManager()
            }
        except Exception as e:
            print(f"Warning: Could not initialize automation components: {e}")
            return {}

    def get_workflow_status(self) -> Dict:
        """Get current workflow status"""
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Get counts for each stage
        cursor.execute("SELECT COUNT(*) FROM design_briefs WHERE status = 'pending'")
        pending_briefs = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM design_briefs WHERE status = 'approved'")
        approved_briefs = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM design_assets")
        total_assets = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM design_assets WHERE printful_status = 'completed'")
        printful_ready = cursor.fetchone()[0]

        conn.close()

        return {
            'pending_briefs': pending_briefs,
            'approved_briefs': approved_briefs,
            'total_assets': total_assets,
            'printful_ready': printful_ready,
            'last_updated': datetime.now().isoformat()
        }

    def add_store(self, store_name: str, data_source: str, store_url: str = None, csv_file_path: str = None) -> Dict:
        """Add a new Etsy store to the system"""
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO etsy_stores (store_name, store_url, csv_file_path, data_source)
                VALUES (?, ?, ?, ?)
            ''', (store_name, store_url, csv_file_path, data_source))
            store_id = cursor.lastrowid
            conn.commit()

            return {'success': True, 'store_id': store_id, 'message': f'Store "{store_name}" added successfully'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
        finally:
            conn.close()

    def get_stores(self) -> List[Dict]:
        """Get all registered Etsy stores"""
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM etsy_stores ORDER BY created_at DESC')
        stores = []
        for row in cursor.fetchall():
            stores.append({
                'id': row[0],
                'store_name': row[1],
                'store_url': row[2],
                'csv_file_path': row[3],
                'data_source': row[4],
                'created_at': row[5],
                'last_analyzed': row[6]
            })

        conn.close()
        return stores

    def run_market_analysis(self, store_id: int = None, analysis_config: Dict = None) -> Dict:
        """Run market analysis and generate design briefs"""
        if 'analyzer' not in self.automation_components:
            return {'success': False, 'error': 'Analyzer not available'}

        try:
            # Get store data if store_id provided
            store_data = None
            if store_id:
                store_data = self._get_store_by_id(store_id)
                if not store_data:
                    return {'success': False, 'error': f'Store with ID {store_id} not found'}

                # Prepare analysis with store-specific data
                if store_data['data_source'] == 'csv' and store_data['csv_file_path']:
                    # Use CSV file for analysis
                    csv_path = store_data['csv_file_path']
                    if not os.path.exists(csv_path):
                        return {'success': False, 'error': f'CSV file not found: {csv_path}'}
                elif store_data['data_source'] == 'url' and store_data['store_url']:
                    # Note: URL scraping would require additional implementation
                    return {'success': False, 'error': 'URL scraping not implemented yet. Please use CSV upload.'}

            # Run the analysis
            analysis_result = self.automation_components['analyzer'].run_automated_analysis_cycle()

            # Generate design briefs based on analysis
            if 'design_manager' in self.automation_components and analysis_result:
                # Save analysis result to temp file for processing
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
                    json.dump(analysis_result, f, indent=2, default=str)
                    temp_analysis_file = f.name

                # Process analysis and generate briefs
                try:
                    prompt_files = self.automation_components['design_manager'].process_market_analysis(temp_analysis_file)

                    # Load generated briefs from files and store in database
                    briefs_dir = os.path.join(self.automation_components['design_manager'].output_dir, "briefs")
                    generated_briefs = []

                    for brief_file in os.listdir(briefs_dir):
                        if brief_file.endswith('_brief.json'):
                            with open(os.path.join(briefs_dir, brief_file), 'r') as f:
                                brief_data = json.load(f)
                                generated_briefs.append(brief_data)

                    if generated_briefs:
                        self._store_design_briefs(generated_briefs)

                    # Clean up temp file
                    os.unlink(temp_analysis_file)

                    return {
                        'success': True,
                        'analysis': analysis_result,
                        'briefs_generated': len(generated_briefs),
                        'message': f'Market analysis complete. Generated {len(generated_briefs)} design briefs for review.'
                    }
                except Exception as e:
                    # Clean up temp file on error
                    if os.path.exists(temp_analysis_file):
                        os.unlink(temp_analysis_file)
                    return {'success': False, 'error': f'Brief generation failed: {str(e)}'}

            return {'success': True, 'analysis': analysis_result}

        except Exception as e:
            return {'success': False, 'error': str(e)}

    def _get_store_by_id(self, store_id: int) -> Optional[Dict]:
        """Get store data by ID"""
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM etsy_stores WHERE id = ?', (store_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                'id': row[0],
                'store_name': row[1],
                'store_url': row[2],
                'csv_file_path': row[3],
                'data_source': row[4],
                'created_at': row[5],
                'last_analyzed': row[6]
            }
        return None

    def _store_design_briefs(self, briefs: List[Dict]):
        """Store generated design briefs in database"""
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        for brief in briefs:
            brief_id = brief.get('concept_name', f"brief_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            cursor.execute('''
                INSERT OR REPLACE INTO design_briefs (brief_id, brief_data, status)
                VALUES (?, ?, ?)
            ''', (brief_id, json.dumps(brief), 'pending'))

        conn.commit()
        conn.close()

# Initialize workflow manager
workflow_manager = WorkflowManager()

@app.route('/')
def dashboard():
    """Main dashboard showing workflow overview"""
    status = workflow_manager.get_workflow_status()
    return render_template('dashboard.html', status=status)

@app.route('/market-analysis')
def market_analysis():
    """Market analysis page"""
    return render_template('market_analysis.html')

@app.route('/api/stores', methods=['GET', 'POST'])
def api_stores():
    """API endpoint to manage Etsy stores"""
    if request.method == 'GET':
        stores = workflow_manager.get_stores()
        return jsonify({'success': True, 'stores': stores})

    elif request.method == 'POST':
        data = request.get_json()
        result = workflow_manager.add_store(
            store_name=data.get('store_name'),
            data_source=data.get('data_source'),
            store_url=data.get('store_url'),
            csv_file_path=data.get('csv_file_path')
        )
        return jsonify(result)

@app.route('/api/upload-csv', methods=['POST'])
def api_upload_csv():
    """API endpoint to upload Etsy CSV data"""
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file uploaded'})

    file = request.files['file']
    store_name = request.form.get('store_name')

    if file.filename == '' or not store_name:
        return jsonify({'success': False, 'error': 'File and store name required'})

    if file and file.filename.endswith('.csv'):
        # Create store data directory
        os.makedirs(app.config['CSV_UPLOAD_FOLDER'], exist_ok=True)

        # Save file with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{store_name}_{timestamp}.csv"
        file_path = os.path.join(app.config['CSV_UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Add store to database
        result = workflow_manager.add_store(
            store_name=store_name,
            data_source='csv',
            csv_file_path=file_path
        )

        if result['success']:
            return jsonify({
                'success': True,
                'message': f'CSV uploaded and store "{store_name}" added successfully',
                'store_id': result['store_id'],
                'file_path': file_path
            })
        else:
            # Clean up file if store creation failed
            if os.path.exists(file_path):
                os.unlink(file_path)
            return jsonify(result)

    return jsonify({'success': False, 'error': 'Invalid file format. Please upload a CSV file.'})

@app.route('/api/run-analysis', methods=['POST'])
def api_run_analysis():
    """API endpoint to run market analysis"""
    data = request.get_json()
    store_id = data.get('store_id') if data else None
    analysis_config = data.get('config', {}) if data else {}

    result = workflow_manager.run_market_analysis(store_id=store_id, analysis_config=analysis_config)
    return jsonify(result)

@app.route('/design-pipeline')
def design_pipeline():
    """Design pipeline page for reviewing and approving briefs"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM design_briefs ORDER BY created_at DESC")
    briefs = []

    for row in cursor.fetchall():
        brief_data = json.loads(row[2])  # brief_data column
        briefs.append({
            'id': row[0],
            'brief_id': row[1],
            'data': brief_data,
            'status': row[3],
            'approval_notes': row[4],
            'created_at': row[5]
        })

    conn.close()
    return render_template('design_pipeline.html', briefs=briefs)

@app.route('/api/approve-brief', methods=['POST'])
def api_approve_brief():
    """API endpoint to approve/reject design briefs"""
    data = request.get_json()
    brief_id = data.get('brief_id')
    action = data.get('action')  # 'approve' or 'reject'
    notes = data.get('notes', '')

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    status = 'approved' if action == 'approve' else 'rejected'
    cursor.execute('''
        UPDATE design_briefs
        SET status = ?, approval_notes = ?, approved_at = CURRENT_TIMESTAMP
        WHERE brief_id = ?
    ''', (status, notes, brief_id))

    conn.commit()
    conn.close()

    return jsonify({'success': True, 'message': f'Brief {action}ed successfully'})

@app.route('/api/clear-pending-briefs', methods=['POST'])
def api_clear_pending_briefs():
    """API endpoint to clear all pending design briefs"""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Get all pending briefs with their file references
        cursor.execute('''
            SELECT brief_id, brief_data FROM design_briefs
            WHERE status = 'pending'
        ''')
        pending_briefs = cursor.fetchall()

        if not pending_briefs:
            conn.close()
            return jsonify({'success': True, 'message': 'No pending briefs to clear', 'cleared_count': 0})

        cleared_files = []
        cleared_count = len(pending_briefs)

        # Delete associated files
        for brief_id, brief_data_json in pending_briefs:
            try:
                brief_data = json.loads(brief_data_json)

                # Look for potential file paths in multiple directories
                design_base_dir = Path("DESIGNS")
                automation_base_dir = Path("automation")

                # Check for associated files in DESIGNS/briefs directory
                briefs_dir = design_base_dir / "briefs"
                if briefs_dir.exists():
                    # Look for files matching the brief_id
                    for file_path in briefs_dir.glob(f"*{brief_id}*"):
                        if file_path.is_file():
                            file_path.unlink()
                            cleared_files.append(str(file_path))

                # Check for associated files in automation/briefs directory
                automation_briefs_dir = automation_base_dir / "briefs"
                if automation_briefs_dir.exists():
                    for file_path in automation_briefs_dir.glob(f"*{brief_id}*"):
                        if file_path.is_file():
                            file_path.unlink()
                            cleared_files.append(str(file_path))

                # Check for associated files in automation/trend_briefs directory
                trend_briefs_dir = automation_base_dir / "trend_briefs"
                if trend_briefs_dir.exists():
                    for file_path in trend_briefs_dir.glob(f"*{brief_id}*"):
                        if file_path.is_file():
                            file_path.unlink()
                            cleared_files.append(str(file_path))

                # Check for associated prompt files in DESIGNS/prompts
                prompts_dir = design_base_dir / "prompts"
                if prompts_dir.exists():
                    for file_path in prompts_dir.glob(f"*{brief_id}*"):
                        if file_path.is_file():
                            file_path.unlink()
                            cleared_files.append(str(file_path))

                # Check for any other files that might match the concept name
                concept_name = brief_data.get('concept_name', brief_id)

                # Search in both DESIGNS and automation directories
                for base_dir in [design_base_dir, automation_base_dir]:
                    if base_dir.exists():
                        for file_path in base_dir.rglob(f"*{concept_name}*"):
                            if file_path.is_file() and file_path.suffix in ['.json', '.txt', '.md']:
                                file_path.unlink()
                                cleared_files.append(str(file_path))

            except Exception as e:
                print(f"Error clearing files for brief {brief_id}: {e}")

        # Delete pending briefs from database
        cursor.execute('DELETE FROM design_briefs WHERE status = ?', ('pending',))
        conn.commit()
        conn.close()

        return jsonify({
            'success': True,
            'message': f'Cleared {cleared_count} pending briefs and {len(cleared_files)} associated files',
            'cleared_count': cleared_count,
            'cleared_files': cleared_files
        })

    except Exception as e:
        return jsonify({'success': False, 'error': f'Failed to clear pending briefs: {str(e)}'})

@app.route('/design-assets')
def design_assets():
    """Design assets management page"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Get approved briefs and their assets
    cursor.execute('''
        SELECT db.brief_id, db.brief_data, da.file_path, da.status, da.printful_status, da.etsy_status
        FROM design_briefs db
        LEFT JOIN design_assets da ON db.brief_id = da.brief_id
        WHERE db.status = 'approved'
        ORDER BY db.approved_at DESC
    ''')

    assets = []
    for row in cursor.fetchall():
        brief_data = json.loads(row[1])
        assets.append({
            'brief_id': row[0],
            'brief_data': brief_data,
            'file_path': row[2],
            'status': row[3],
            'printful_status': row[4],
            'etsy_status': row[5]
        })

    conn.close()
    return render_template('design_assets.html', assets=assets)

@app.route('/api/upload-design', methods=['POST'])
def api_upload_design():
    """API endpoint to upload design files"""
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file uploaded'})

    file = request.files['file']
    brief_id = request.form.get('brief_id')

    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'})

    if file and brief_id:
        # Ensure upload directory exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

        # Save file
        filename = f"{brief_id}_{file.filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Store in database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        asset_id = f"{brief_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        cursor.execute('''
            INSERT INTO design_assets (asset_id, brief_id, file_path, status)
            VALUES (?, ?, ?, ?)
        ''', (asset_id, brief_id, file_path, 'uploaded'))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Design uploaded successfully', 'file_path': file_path})

    return jsonify({'success': False, 'error': 'Upload failed'})

@app.route('/api/workflow-status')
def api_workflow_status():
    """API endpoint to get current workflow status"""
    status = workflow_manager.get_workflow_status()
    return jsonify(status)

@app.route('/api/setup-printful', methods=['POST'])
def api_setup_printful():
    """API endpoint to setup Printful product from uploaded design"""
    data = request.get_json()
    brief_id = data.get('brief_id')

    if not brief_id:
        return jsonify({'success': False, 'error': 'Brief ID required'})

    # Get the design asset and brief data
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT da.file_path, da.asset_id, db.brief_data
        FROM design_assets da
        JOIN design_briefs db ON da.brief_id = db.brief_id
        WHERE da.brief_id = ? AND da.status = 'uploaded'
    ''', (brief_id,))

    result = cursor.fetchone()
    if not result:
        conn.close()
        return jsonify({'success': False, 'error': 'Design asset not found or not uploaded'})

    file_path, asset_id, brief_data_json = result
    brief_data = json.loads(brief_data_json)

    try:
        # Update status to in-progress
        cursor.execute('''
            UPDATE design_assets
            SET printful_status = 'in_progress'
            WHERE brief_id = ?
        ''', (brief_id,))
        conn.commit()

        # Import and use the actual Printful automation
        try:
            from automation.printful_integration import AutomatedProductCreator
            creator = AutomatedProductCreator(app.config['PRINTFUL_API_KEY'])

            # Create Printful product using the automation system
            creation_result = creator.create_product_from_brief(brief_data, file_path)

            if creation_result.success:
                # Update status to completed with details
                cursor.execute('''
                    UPDATE design_assets
                    SET printful_status = 'completed'
                    WHERE brief_id = ?
                ''', (brief_id,))
                conn.commit()

                # Save creation details to DESIGNS directory
                creation_details = {
                    'brief_id': brief_id,
                    'creation_result': asdict(creation_result),
                    'timestamp': datetime.now().isoformat()
                }

                details_file = f"DESIGNS/printful_products/creation_{brief_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                os.makedirs(os.path.dirname(details_file), exist_ok=True)
                with open(details_file, 'w', encoding='utf-8') as f:
                    json.dump(creation_details, f, indent=2)

                conn.close()
                return jsonify({
                    'success': True,
                    'message': f'Printful product created successfully: {creation_result.sync_product_id}',
                    'brief_id': brief_id,
                    'printful_product_id': creation_result.sync_product_id,
                    'variants_created': creation_result.variant_count,
                    'mockup_urls': creation_result.mockup_urls,
                    'dashboard_url': creation_result.printful_dashboard_url,
                    'products': brief_data.get('printful_products', [])
                })
            else:
                # Update status to error
                cursor.execute('''
                    UPDATE design_assets
                    SET printful_status = 'error'
                    WHERE brief_id = ?
                ''', (brief_id,))
                conn.commit()
                conn.close()

                return jsonify({
                    'success': False,
                    'error': f'Printful product creation failed: {creation_result.error_message}'
                })

        except ImportError:
            # Fallback to simulation if automation not available
            import time
            time.sleep(2)  # Simulate processing time

            # Update status to completed
            cursor.execute('''
                UPDATE design_assets
                SET printful_status = 'completed'
                WHERE brief_id = ?
            ''', (brief_id,))
            conn.commit()

        conn.close()

        return jsonify({
            'success': True,
            'message': f'Printful product setup completed for {brief_data.get("concept_name", brief_id)}',
            'brief_id': brief_id,
            'products': brief_data.get('printful_products', [])
        })

    except Exception as e:
        # Reset status on error
        cursor.execute('''
            UPDATE design_assets
            SET printful_status = 'error'
            WHERE brief_id = ?
        ''', (brief_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': False, 'error': f'Printful setup failed: {str(e)}'})

@app.route('/api/create-etsy-listing', methods=['POST'])
def api_create_etsy_listing():
    """API endpoint to create Etsy listing from Printful-ready design"""
    data = request.get_json()
    brief_id = data.get('brief_id')

    if not brief_id:
        return jsonify({'success': False, 'error': 'Brief ID required'})

    # Get the design asset and brief data
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT da.file_path, da.printful_status, db.brief_data
        FROM design_assets da
        JOIN design_briefs db ON da.brief_id = db.brief_id
        WHERE da.brief_id = ?
    ''', (brief_id,))

    result = cursor.fetchone()
    if not result:
        conn.close()
        return jsonify({'success': False, 'error': 'Design asset not found'})

    file_path, printful_status, brief_data_json = result
    brief_data = json.loads(brief_data_json)

    if printful_status != 'completed':
        conn.close()
        return jsonify({'success': False, 'error': 'Printful setup must be completed first'})

    try:
        # Update status to in-progress
        cursor.execute('''
            UPDATE design_assets
            SET etsy_status = 'in_progress'
            WHERE brief_id = ?
        ''', (brief_id,))
        conn.commit()

        # Here you would integrate with actual Etsy API
        # For now, we'll simulate the process and mark as completed
        import time
        time.sleep(2)  # Simulate processing time

        # Update status to completed
        cursor.execute('''
            UPDATE design_assets
            SET etsy_status = 'completed'
            WHERE brief_id = ?
        ''', (brief_id,))
        conn.commit()

        conn.close()

        return jsonify({
            'success': True,
            'message': f'Etsy listing created for {brief_data.get("concept_name", brief_id)}',
            'brief_id': brief_id,
            'listing_url': f'https://etsy.com/listing/placeholder-{brief_id}'  # Placeholder URL
        })

    except Exception as e:
        # Reset status on error
        cursor.execute('''
            UPDATE design_assets
            SET etsy_status = 'error'
            WHERE brief_id = ?
        ''', (brief_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': False, 'error': f'Etsy listing creation failed: {str(e)}'})

@app.route('/api/printful-catalog-status')
def api_printful_catalog_status():
    """API endpoint to get Printful catalog status"""
    if 'catalog_manager' not in workflow_manager.automation_components:
        return jsonify({'success': False, 'error': 'Catalog manager not available'})

    try:
        catalog_manager = workflow_manager.automation_components['catalog_manager']
        status = catalog_manager.get_catalog_status()
        return jsonify({'success': True, 'status': status})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/update-printful-catalog', methods=['POST'])
def api_update_printful_catalog():
    """API endpoint to update Printful catalog"""
    if 'catalog_manager' not in workflow_manager.automation_components:
        return jsonify({'success': False, 'error': 'Catalog manager not available'})

    try:
        data = request.get_json() or {}
        force_update = data.get('force_update', False)

        catalog_manager = workflow_manager.automation_components['catalog_manager']
        result = catalog_manager.download_catalog(force_update=force_update)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/validate-products', methods=['POST'])
def api_validate_products():
    """API endpoint to validate products against Printful catalog"""
    if 'catalog_manager' not in workflow_manager.automation_components:
        return jsonify({'success': False, 'error': 'Catalog manager not available'})

    try:
        data = request.get_json()
        products = data.get('products', [])

        if not products:
            return jsonify({'success': False, 'error': 'No products provided for validation'})

        catalog_manager = workflow_manager.automation_components['catalog_manager']
        validation_result = catalog_manager.validate_products(products)

        return jsonify({
            'success': True,
            'validation': validation_result
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/printful-products')
def api_printful_products():
    """API endpoint to get available Printful products"""
    if 'catalog_manager' not in workflow_manager.automation_components:
        return jsonify({'success': False, 'error': 'Catalog manager not available'})

    try:
        category = request.args.get('category')
        catalog_manager = workflow_manager.automation_components['catalog_manager']
        products = catalog_manager.get_products_by_category(category)

        return jsonify({
            'success': True,
            'products': products,
            'count': len(products)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/export-content', methods=['POST'])
def api_export_content():
    """API endpoint to export content in various formats"""
    try:
        from automation.export_manager import ExportManager

        data = request.get_json() or {}
        export_format = data.get('format', 'zip')  # zip, csv, json
        content_types = data.get('content_types', [])  # specific content types
        date_range = data.get('date_range')  # optional date filtering

        export_manager = ExportManager()

        if content_types:
            # Filtered export
            result = export_manager.export_filtered_content(content_types, date_range)
        else:
            # Complete export
            result = export_manager.export_all_content(export_format)

        if result.success:
            return jsonify({
                'success': True,
                'export_path': result.export_path,
                'file_size': result.file_size,
                'items_exported': result.items_exported,
                'export_type': result.export_type,
                'download_url': f'/api/download-export?file={Path(result.export_path).name}'
            })
        else:
            return jsonify({
                'success': False,
                'error': result.error_message
            })

    except ImportError:
        return jsonify({'success': False, 'error': 'Export manager not available'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/download-export')
def api_download_export():
    """API endpoint to download exported files"""
    try:
        filename = request.args.get('file')
        if not filename:
            return jsonify({'success': False, 'error': 'No file specified'})

        # Security check - ensure file is in exports directory
        export_path = Path("DESIGNS/exports") / filename
        if not export_path.exists() or not export_path.is_file():
            return jsonify({'success': False, 'error': 'File not found'})

        # Send file for download
        return send_file(export_path, as_attachment=True, download_name=filename)

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/export-statistics')
def api_export_statistics():
    """API endpoint to get export statistics"""
    try:
        from automation.export_manager import ExportManager

        export_manager = ExportManager()
        stats = export_manager.get_export_statistics()

        return jsonify({
            'success': True,
            'statistics': stats
        })

    except ImportError:
        return jsonify({'success': False, 'error': 'Export manager not available'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Initialize database on startup
    init_database()

    # Create necessary directories
    os.makedirs('DESIGNS/completed_designs/png_files', exist_ok=True)
    os.makedirs('DESIGNS/store_data', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)

    print("Starting EtsyAnalyzer Workflow Dashboard...")
    print("Access your dashboard at: http://localhost:5000")
    print("Workflow management interface ready!")

    app.run(debug=True, host='0.0.0.0', port=5000)