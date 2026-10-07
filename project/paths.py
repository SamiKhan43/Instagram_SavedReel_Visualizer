from pathlib import Path
 
class Paths:
    ROOT = Path(__file__).parent #__file__ is a special python variable that contain the path of the current python file  

    #data directories
    DATA_DIR = ROOT / "data" #means add data dir in our current dir
    OUT_DIR = DATA_DIR / "Outputs" #same logic as data dir
    INPUT_FILE = DATA_DIR / "saved_posts.json"
    RAW_CACHE = OUT_DIR / "apify_raw_results.json"
    CSV_FILE = OUT_DIR / "saved_reels_enriched_data.csv"
    MD_FILE = OUT_DIR / "visual_roadmap.md"

    @classmethod
    def ensure_dirs_exist(cls):
        #When you call Paths.ensure_dirs_exist(), Python automatically sets cls = Paths.

        cls.DATA_DIR.mkdir(parents=True , exist_ok = True) 
        cls.OUT_DIR.mkdir(parents=True , exist_ok = True)
        #if exist dont gave error

    @classmethod   #-> bool its a type hint means the fuc will return a bool
    def validate_input(cls) -> bool: 
        if cls.INPUT_FILE.exists():
            return True
        return False
    
    @classmethod 
    def get_summary(cls) -> str:  #Return a readable summary of all paths
        return f"""
        Project Paths:
        - Root: {cls.ROOT}
        - Data Dir: {cls.DATA_DIR}
        - Output Dir: {cls.OUT_DIR}
        - Input File: {cls.INPUT_FILE}
        - Raw Cache: {cls.RAW_CACHE}
        - CSV Output: {cls.CSV_FILE}
        - Markdown Output: {cls.MD_FILE}
        """ 
