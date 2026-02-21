#!/usr/bin/env python3
"""
Export Manager for EtsyAnalyzer
Provides comprehensive export and download functionality for all generated content
"""

import os
# Force UTF-8 encoding for all operations
os.environ['PYTHONIOENCODING'] = 'utf-8'

import json
import csv
import zipfile
import shutil
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path
import pandas as pd

@dataclass
class ExportSpec:
    """Specification for an export operation"""
    export_type: str  # csv, json, zip, pdf
    content_types: List[str]  # briefs, listings, analysis, etc.
    date_range: Optional[Dict[str, str]]
    filters: Dict[str, Any]
    output_filename: str

@dataclass
class ExportResult:
    """Result of an export operation"""
    success: bool
    export_path: str
    file_size: int
    items_exported: int
    export_type: str
    error_message: Optional[str]
    generated_timestamp: str

class ExportManager:
    """Manages export and download functionality for all EtsyAnalyzer content"""

    def __init__(self, base_path: str = "DESIGNS"):
        self.base_path = Path(base_path)
        self.export_path = self.base_path / "exports"
        self.export_path.mkdir(exist_ok=True)

        # Content type mappings
        self.content_mappings = {
            "briefs": {
                "directory": "briefs",
                "pattern": "*_brief.json",
                "type": "design_briefs"
            },
            "listings": {
                "directory": "etsy_listings",
                "pattern": "*_etsy_listing.json",
                "type": "etsy_listings"
            },
            "analysis": {
                "directory": "automated_outputs",
                "pattern": "*.json",
                "type": "market_analysis"
            },
            "prompts": {
                "directory": "prompts",
                "pattern": "*.txt",
                "type": "design_prompts"
            },
            "printful": {
                "directory": "printful_products",
                "pattern": "*.json",
                "type": "printful_products"
            },
            "seo": {
                "directory": "seo_recommendations",
                "pattern": "*.json",
                "type": "seo_recommendations"
            }
        }

    def export_all_content(self, export_format: str = "zip") -> ExportResult:
        """Export all content in specified format"""

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if export_format == "zip":
            return self._export_complete_archive(timestamp)
        elif export_format == "csv":
            return self._export_csv_summary(timestamp)
        elif export_format == "json":
            return self._export_json_summary(timestamp)
        else:
            return ExportResult(
                success=False,
                export_path="",
                file_size=0,
                items_exported=0,
                export_type=export_format,
                error_message=f"Unsupported export format: {export_format}",
                generated_timestamp=datetime.now().isoformat()
            )

    def _export_complete_archive(self, timestamp: str) -> ExportResult:
        """Create a complete ZIP archive of all content"""

        try:
            zip_filename = f"etsy_analyzer_complete_export_{timestamp}.zip"
            zip_path = self.export_path / zip_filename

            items_exported = 0

            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Add all content directories
                for content_type, mapping in self.content_mappings.items():
                    content_dir = self.base_path / mapping["directory"]
                    if content_dir.exists():
                        # Add directory and all files
                        for file_path in content_dir.rglob("*"):
                            if file_path.is_file():
                                arcname = file_path.relative_to(self.base_path)
                                zipf.write(file_path, arcname)
                                items_exported += 1

                # Add summary report
                summary = self._generate_export_summary()
                summary_json = json.dumps(summary, indent=2, ensure_ascii=False)
                zipf.writestr("export_summary.json", summary_json)
                items_exported += 1

                # Add CSV data export
                csv_data = self._generate_csv_data()
                zipf.writestr("data_export.csv", csv_data)
                items_exported += 1

            file_size = zip_path.stat().st_size

            return ExportResult(
                success=True,
                export_path=str(zip_path),
                file_size=file_size,
                items_exported=items_exported,
                export_type="zip",
                error_message=None,
                generated_timestamp=datetime.now().isoformat()
            )

        except Exception as e:
            return ExportResult(
                success=False,
                export_path="",
                file_size=0,
                items_exported=0,
                export_type="zip",
                error_message=str(e),
                generated_timestamp=datetime.now().isoformat()
            )

    def _export_csv_summary(self, timestamp: str) -> ExportResult:
        """Export a CSV summary of all content"""

        try:
            csv_filename = f"etsy_analyzer_summary_{timestamp}.csv"
            csv_path = self.export_path / csv_filename

            # Collect all data
            all_data = []

            # Process briefs
            briefs_data = self._collect_briefs_data()
            all_data.extend(briefs_data)

            # Process listings
            listings_data = self._collect_listings_data()
            all_data.extend(listings_data)

            # Process analysis
            analysis_data = self._collect_analysis_data()
            all_data.extend(analysis_data)

            # Write CSV
            if all_data:
                df = pd.DataFrame(all_data)
                df.to_csv(csv_path, index=False, encoding='utf-8')
                items_exported = len(all_data)
            else:
                # Create empty CSV with headers
                headers = ['type', 'name', 'created_date', 'status', 'details']
                with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)
                items_exported = 0

            file_size = csv_path.stat().st_size

            return ExportResult(
                success=True,
                export_path=str(csv_path),
                file_size=file_size,
                items_exported=items_exported,
                export_type="csv",
                error_message=None,
                generated_timestamp=datetime.now().isoformat()
            )

        except Exception as e:
            return ExportResult(
                success=False,
                export_path="",
                file_size=0,
                items_exported=0,
                export_type="csv",
                error_message=str(e),
                generated_timestamp=datetime.now().isoformat()
            )

    def _export_json_summary(self, timestamp: str) -> ExportResult:
        """Export a JSON summary of all content"""

        try:
            json_filename = f"etsy_analyzer_summary_{timestamp}.json"
            json_path = self.export_path / json_filename

            # Generate comprehensive summary
            summary = {
                "export_metadata": {
                    "generated_timestamp": datetime.now().isoformat(),
                    "export_type": "json_summary",
                    "base_path": str(self.base_path),
                    "version": "1.0"
                },
                "content_summary": self._generate_export_summary(),
                "briefs": self._collect_briefs_data(),
                "listings": self._collect_listings_data(),
                "analysis": self._collect_analysis_data(),
                "printful_products": self._collect_printful_data(),
                "seo_recommendations": self._collect_seo_data()
            }

            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False, default=str)

            items_exported = sum(len(summary[key]) for key in ['briefs', 'listings', 'analysis', 'printful_products', 'seo_recommendations'] if isinstance(summary.get(key), list))
            file_size = json_path.stat().st_size

            return ExportResult(
                success=True,
                export_path=str(json_path),
                file_size=file_size,
                items_exported=items_exported,
                export_type="json",
                error_message=None,
                generated_timestamp=datetime.now().isoformat()
            )

        except Exception as e:
            return ExportResult(
                success=False,
                export_path="",
                file_size=0,
                items_exported=0,
                export_type="json",
                error_message=str(e),
                generated_timestamp=datetime.now().isoformat()
            )

    def _generate_export_summary(self) -> Dict[str, Any]:
        """Generate a comprehensive export summary"""

        summary = {
            "generated_timestamp": datetime.now().isoformat(),
            "content_statistics": {},
            "directory_structure": {},
            "file_counts": {},
            "total_size": 0
        }

        total_size = 0

        for content_type, mapping in self.content_mappings.items():
            content_dir = self.base_path / mapping["directory"]

            if content_dir.exists():
                files = list(content_dir.rglob("*"))
                file_count = len([f for f in files if f.is_file()])
                dir_size = sum(f.stat().st_size for f in files if f.is_file())

                summary["content_statistics"][content_type] = {
                    "file_count": file_count,
                    "directory_size": dir_size,
                    "directory_path": str(content_dir.relative_to(self.base_path))
                }

                summary["file_counts"][content_type] = file_count
                total_size += dir_size
            else:
                summary["content_statistics"][content_type] = {
                    "file_count": 0,
                    "directory_size": 0,
                    "directory_path": str(Path(mapping["directory"]))
                }
                summary["file_counts"][content_type] = 0

        summary["total_size"] = total_size

        # Add workflow statistics
        summary["workflow_statistics"] = {
            "total_briefs": summary["file_counts"].get("briefs", 0),
            "total_listings": summary["file_counts"].get("listings", 0),
            "total_analysis": summary["file_counts"].get("analysis", 0),
            "total_printful_products": summary["file_counts"].get("printful", 0),
            "completion_rate": self._calculate_completion_rate()
        }

        return summary

    def _calculate_completion_rate(self) -> float:
        """Calculate workflow completion rate"""

        try:
            briefs_count = len(list((self.base_path / "briefs").glob("*_brief.json"))) if (self.base_path / "briefs").exists() else 0
            listings_count = len(list((self.base_path / "etsy_listings").glob("*_listing.json"))) if (self.base_path / "etsy_listings").exists() else 0

            if briefs_count == 0:
                return 0.0

            completion_rate = (listings_count / briefs_count) * 100
            return min(completion_rate, 100.0)

        except Exception:
            return 0.0

    def _collect_briefs_data(self) -> List[Dict[str, Any]]:
        """Collect all design briefs data"""

        briefs_data = []
        briefs_dir = self.base_path / "briefs"

        if briefs_dir.exists():
            for brief_file in briefs_dir.glob("*_brief.json"):
                try:
                    with open(brief_file, 'r', encoding='utf-8') as f:
                        brief_data = json.load(f)

                    briefs_data.append({
                        "type": "design_brief",
                        "name": brief_data.get("concept_name", brief_file.stem),
                        "created_date": brief_file.stat().st_mtime,
                        "theme": brief_data.get("design_theme", "unknown"),
                        "target_audience": brief_data.get("target_audience", ""),
                        "printful_products": ", ".join(brief_data.get("printful_products", [])),
                        "priority_score": brief_data.get("priority_score", 0),
                        "file_path": str(brief_file.relative_to(self.base_path))
                    })

                except Exception as e:
                    print(f"Error processing brief {brief_file}: {e}")

        return briefs_data

    def _collect_listings_data(self) -> List[Dict[str, Any]]:
        """Collect all Etsy listings data"""

        listings_data = []
        listings_dir = self.base_path / "etsy_listings"

        if listings_dir.exists():
            for listing_file in listings_dir.glob("*_etsy_listing.json"):
                try:
                    with open(listing_file, 'r', encoding='utf-8') as f:
                        listing_data = json.load(f)

                    listing_spec = listing_data.get("listing_specification", {})
                    seo_analysis = listing_data.get("seo_analysis", {})

                    listings_data.append({
                        "type": "etsy_listing",
                        "name": listing_spec.get("title", listing_file.stem),
                        "created_date": listing_file.stat().st_mtime,
                        "price": listing_spec.get("price", 0),
                        "category_id": listing_spec.get("category_id", 0),
                        "tags_count": len(listing_spec.get("tags", [])),
                        "seo_score": seo_analysis.get("overall_score", 0),
                        "target_keywords": ", ".join(listing_spec.get("target_keywords", [])),
                        "file_path": str(listing_file.relative_to(self.base_path))
                    })

                except Exception as e:
                    print(f"Error processing listing {listing_file}: {e}")

        return listings_data

    def _collect_analysis_data(self) -> List[Dict[str, Any]]:
        """Collect all analysis data"""

        analysis_data = []
        analysis_dir = self.base_path / "automated_outputs"

        if analysis_dir.exists():
            for analysis_file in analysis_dir.glob("*.json"):
                try:
                    with open(analysis_file, 'r', encoding='utf-8') as f:
                        analysis = json.load(f)

                    analysis_data.append({
                        "type": "market_analysis",
                        "name": analysis_file.stem,
                        "created_date": analysis_file.stat().st_mtime,
                        "status": analysis.get("status", "unknown"),
                        "workflows_executed": analysis.get("automation_results", {}).get("total_workflows_executed", 0),
                        "outputs_generated": analysis.get("automation_results", {}).get("total_outputs_generated", 0),
                        "file_path": str(analysis_file.relative_to(self.base_path))
                    })

                except Exception as e:
                    print(f"Error processing analysis {analysis_file}: {e}")

        return analysis_data

    def _collect_printful_data(self) -> List[Dict[str, Any]]:
        """Collect all Printful product data"""

        printful_data = []
        printful_dir = self.base_path / "printful_products"

        if printful_dir.exists():
            for printful_file in printful_dir.glob("*.json"):
                try:
                    with open(printful_file, 'r', encoding='utf-8') as f:
                        product_data = json.load(f)

                    creation_result = product_data.get("creation_result", {})

                    printful_data.append({
                        "type": "printful_product",
                        "name": printful_file.stem,
                        "created_date": printful_file.stat().st_mtime,
                        "success": creation_result.get("success", False),
                        "product_id": creation_result.get("product_id", ""),
                        "sync_product_id": creation_result.get("sync_product_id", ""),
                        "variant_count": creation_result.get("variant_count", 0),
                        "file_path": str(printful_file.relative_to(self.base_path))
                    })

                except Exception as e:
                    print(f"Error processing Printful product {printful_file}: {e}")

        return printful_data

    def _collect_seo_data(self) -> List[Dict[str, Any]]:
        """Collect all SEO recommendation data"""

        seo_data = []
        seo_dir = self.base_path / "seo_recommendations"

        if seo_dir.exists():
            for seo_file in seo_dir.glob("*.json"):
                try:
                    with open(seo_file, 'r', encoding='utf-8') as f:
                        seo_recommendations = json.load(f)

                    seo_data.append({
                        "type": "seo_recommendations",
                        "name": seo_file.stem,
                        "created_date": seo_file.stat().st_mtime,
                        "current_seo_score": seo_recommendations.get("current_seo_score", 0),
                        "target_seo_score": seo_recommendations.get("target_seo_score", 0),
                        "optimization_actions": len(seo_recommendations.get("optimization_actions", [])),
                        "file_path": str(seo_file.relative_to(self.base_path))
                    })

                except Exception as e:
                    print(f"Error processing SEO recommendations {seo_file}: {e}")

        return seo_data

    def _generate_csv_data(self) -> str:
        """Generate CSV data for all content"""

        all_data = []

        # Collect all data types
        all_data.extend(self._collect_briefs_data())
        all_data.extend(self._collect_listings_data())
        all_data.extend(self._collect_analysis_data())
        all_data.extend(self._collect_printful_data())
        all_data.extend(self._collect_seo_data())

        if not all_data:
            return "type,name,created_date,status,file_path\n"

        # Convert to CSV
        import io
        output = io.StringIO()

        if all_data:
            # Get all unique keys
            all_keys = set()
            for item in all_data:
                all_keys.update(item.keys())

            fieldnames = sorted(all_keys)

            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)

        return output.getvalue()

    def export_filtered_content(self, content_types: List[str], date_range: Dict[str, str] = None) -> ExportResult:
        """Export filtered content based on types and date range"""

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"etsy_analyzer_filtered_export_{timestamp}.zip"
        zip_path = self.export_path / zip_filename

        try:
            items_exported = 0

            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for content_type in content_types:
                    if content_type in self.content_mappings:
                        mapping = self.content_mappings[content_type]
                        content_dir = self.base_path / mapping["directory"]

                        if content_dir.exists():
                            for file_path in content_dir.glob(mapping["pattern"]):
                                if file_path.is_file():
                                    # Apply date filter if specified
                                    if date_range:
                                        file_mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                                        if not self._is_in_date_range(file_mtime, date_range):
                                            continue

                                    arcname = file_path.relative_to(self.base_path)
                                    zipf.write(file_path, arcname)
                                    items_exported += 1

            file_size = zip_path.stat().st_size

            return ExportResult(
                success=True,
                export_path=str(zip_path),
                file_size=file_size,
                items_exported=items_exported,
                export_type="filtered_zip",
                error_message=None,
                generated_timestamp=datetime.now().isoformat()
            )

        except Exception as e:
            return ExportResult(
                success=False,
                export_path="",
                file_size=0,
                items_exported=0,
                export_type="filtered_zip",
                error_message=str(e),
                generated_timestamp=datetime.now().isoformat()
            )

    def _is_in_date_range(self, file_date: datetime, date_range: Dict[str, str]) -> bool:
        """Check if file date is within specified range"""

        try:
            start_date = datetime.fromisoformat(date_range.get("start", "1900-01-01"))
            end_date = datetime.fromisoformat(date_range.get("end", "2100-12-31"))

            return start_date <= file_date <= end_date

        except Exception:
            return True  # Include file if date parsing fails

    def get_export_statistics(self) -> Dict[str, Any]:
        """Get current export statistics"""

        return {
            "content_summary": self._generate_export_summary(),
            "available_exports": list(self.content_mappings.keys()),
            "export_directory": str(self.export_path),
            "total_content_size": sum(
                stat["directory_size"]
                for stat in self._generate_export_summary()["content_statistics"].values()
            )
        }

def main():
    """Test the export manager"""

    print("📤 Export Manager Test")
    print("=" * 30)

    # Initialize export manager
    export_manager = ExportManager()

    # Get current statistics
    stats = export_manager.get_export_statistics()
    print(f"📊 Content Statistics:")
    for content_type, stat in stats["content_summary"]["content_statistics"].items():
        print(f"  {content_type}: {stat['file_count']} files, {stat['directory_size']} bytes")

    # Test CSV export
    print(f"\n📄 Testing CSV export...")
    csv_result = export_manager.export_all_content("csv")

    if csv_result.success:
        print(f"✅ CSV exported: {csv_result.export_path}")
        print(f"   Items: {csv_result.items_exported}, Size: {csv_result.file_size} bytes")
    else:
        print(f"❌ CSV export failed: {csv_result.error_message}")

    # Test JSON export
    print(f"\n📋 Testing JSON export...")
    json_result = export_manager.export_all_content("json")

    if json_result.success:
        print(f"✅ JSON exported: {json_result.export_path}")
        print(f"   Items: {json_result.items_exported}, Size: {json_result.file_size} bytes")
    else:
        print(f"❌ JSON export failed: {json_result.error_message}")

    # Test ZIP export
    print(f"\n📦 Testing ZIP export...")
    zip_result = export_manager.export_all_content("zip")

    if zip_result.success:
        print(f"✅ ZIP exported: {zip_result.export_path}")
        print(f"   Items: {zip_result.items_exported}, Size: {zip_result.file_size} bytes")
    else:
        print(f"❌ ZIP export failed: {zip_result.error_message}")

if __name__ == "__main__":
    main()