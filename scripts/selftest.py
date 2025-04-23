"""Import test for backend"""
import importlib, pkgutil, sys, pathlib

PKG = "backend"
ROOT = pathlib.Path(__file__).resolve().parents[1] / PKG
sys.path.insert(0, str(ROOT.parent))
failed = []
for module in pkgutil.walk_packages([str(ROOT)], prefix=f"{PKG}."):
    try:
        importlib.import_module(module.name)
    except Exception as e:
        failed.append((module.name, e))
if failed:
    print("❌ Import test failed:")
    for name, err in failed:
        print(f"  {name}: {err}")
    sys.exit(1)
print("✅ All backend modules imported successfully.")
