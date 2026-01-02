import os
import sys

# Add the Code directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Code'))

# Import the premium dashboard and run it
if __name__ == "__main__":
    from Code.app.premium_dashboard import main
    # However, premium_dashboard.py is written as a script, not a function.
    # So we should just execute it.
    
    # Actually, the best way for Streamlit is to just have the file in the root.
    # But to keep the Code/ organization, we can do:
    import runpy
    runpy.run_path(os.path.join(os.path.dirname(__file__), 'Code', 'app', 'premium_dashboard.py'))
