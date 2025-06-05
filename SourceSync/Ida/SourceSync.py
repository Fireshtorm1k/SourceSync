import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "srcsync"))
import ida_idp
import ida_kernwin
import idaapi
import PdbGeneratorPy
from srcsync.TypeExtractor import TypeExtractor
from srcsync.PEDataExtractor import PEDataExtractor
from srcsync.SymbolExtractor import SymbolExtractor
from srcsync.FunctionDataExtractor import FunctionDataExtractor

        
class PdbGenPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_PROC
    comment = "PDBGenerator"
    help = "This is help"
    wanted_name = "PdbGen plugin"
    wanted_hotkey = "Alt-Shift-D"
    ACTION_NAME = "PdbGen:generate"
    ICON_PATH = f"{os.path.dirname(__file__)}/srcsync/ico/pdb.png"
    global PdbGenForm
    PdbGenForm = None
    def load_icon(self, path):
        try:
            pixmap = ida_kernwin.load_custom_icon(path)
            if pixmap != idaapi.BADADDR:
                print(f"[PdbGen] Loaded icon from '{path}'")
                return pixmap
            else:
                print(f"[PdbGen] Failed to load icon from '{path}'")
        except Exception as e:
            print(f"[PdbGen] Exception while loading icon: {e}")
        return 0
    
    def init(self):
        if idaapi.unregister_action(self.ACTION_NAME):
            print("[PdbGen] Old action unregistered.")
        ida_kernwin.create_toolbar('pdbgen', 'PdbGenToolBar')
        action = idaapi.action_desc_t(
            self.ACTION_NAME, 
            "Generate PDB",
            self.ActionHandler(),
            self.wanted_hotkey,
            "Generate PDB for current file",
            self.load_icon(self.ICON_PATH)
        )
        if idaapi.register_action(action):
            print("[PdbGen] Action registered.")
        else:
            print("[PdbGen] Failed to register action.")
            
        if idaapi.attach_action_to_toolbar("MainToolBar", self.ACTION_NAME):
            print("[PdbGen] Button added to toolbar.")
        else:
            print("[PdbGen] Failed to add button to toolbar.")
            
        idaapi.register_timer(1000, lambda: self.add_button())
        return idaapi.PLUGIN_KEEP
    
    def add_button(self):
        if idaapi.attach_action_to_toolbar("pdbgen", self.ACTION_NAME):
            print("[PdbGen] Button added to toolbar.")
        else:
            print("[PdbGen] Failed to add button to toolbar.")
            
    class ActionHandler(idaapi.action_handler_t):
        def activate(self, ctx):
            self.CbGeneratePdb()
            return 1
        
        def CbGeneratePdb(self):
            peDataExtractor = PEDataExtractor()
            pdbInfo = peDataExtractor.GetPdbInfo()
            sectionsData = peDataExtractor.GetSectionsData()
            if len(sectionsData) == 0:
                print("[PdbGen] Failed to get sections")       
                return
            if(pdbInfo is None):
                print("[PdbGen] Failed to get pdbInfo")
                return
            print("[PdbGen] Generating pdb")
            typeExtractor = TypeExtractor()
            typeExtractor.GatherData(ExecuteSync = False)
            
            symbolExtractor = SymbolExtractor(typeExtractor)
            publicSymbolsData = symbolExtractor.GetPublics(ExecuteSync = False)
            globalSymbolsData = symbolExtractor.GetGlobals(ExecuteSync = False)
            
            functionDataExtractor = FunctionDataExtractor(typeExtractor)
            functionsData = functionDataExtractor.GetFunctionsData()
            
            enumsData = typeExtractor.GetEnumsData()
            structsData = typeExtractor.GetStructsData()
            complexTypes = typeExtractor.GetComplexTypesData()
            
            

            if idaapi.inf_is_64bit():
                cpuArchitectureType = PdbGeneratorPy.CpuArchitectureType.X86_64
            else:
                cpuArchitectureType = PdbGeneratorPy.CpuArchitectureType.X86
                
            pdbGenerator = PdbGeneratorPy.PdbGenerator(
                complexTypes, structsData, enumsData, functionsData,
                pdbInfo, sectionsData, publicSymbolsData, globalSymbolsData, cpuArchitectureType)
            
            if pdbGenerator.Generate():
                print("[PdbGen] Pdb generated")       
            else:
                print("[PdbGen] Failed to generate pdb")   
        
        def update(self, ctx):
            try:
                if idaapi.get_root_filename():
                    if ida_idp.ph.id == ida_idp.PLFM_386:
                        return idaapi.AST_ENABLE
                return idaapi.AST_DISABLE
            except Exception as e:
                print(f"[PdbGen] Safe update failed: {e}")
                return idaapi.AST_DISABLE

    


    def run(self, Arg):
        if ida_idp.ph.id != ida_idp.PLFM_386:
            print("[PdbGen] Only x86_64/x86 architecture is supported.")
            return

        if "portable executable" not in idaapi.get_file_type_name().lower():
            print("[PdbGen] Only PE files are supported.")
            return
        
        #global PdbGenForm
        #if not PdbGenForm:
        #    PdbGenForm = PdbGenForm()
        #    PdbGenForm.Show()
    
            
    def term(self):
        pass

def PLUGIN_ENTRY():
    return PdbGenPlugin()