# Clean everything and install
rm -rf build/
rm -rf robusttre.egg-info/
pip install -r requirements.txt
pip install --force-reinstall --no-cache-dir .
