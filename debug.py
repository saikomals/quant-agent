import sys
import os

# Force Python to look in the current directory
sys.path.append(os.getcwd())

print("✅ Python is running.")

try:
    from src.audit.schemas import EvidenceBundle
    print("✅ Imported EvidenceBundle successfully.")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("Make sure your folders (src, audit) have empty __init__.py files!")
except Exception as e:
    print(f"❌ Other error: {e}")

try:
    import typer
    print("✅ Typer is installed.")
except ImportError:
    print("❌ Typer is NOT installed. Run: pip install typer")