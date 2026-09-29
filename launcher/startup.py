"""Windows startup entry point."""
import launcher_state, startup_ui, tray
import sys

from PySide6.QtWidgets import QApplication

def startup_fn():
    global tray_controller
    ui = startup_ui.StartupUI()
    tray_controller = tray.GesturaTray(ui)
    result = ui.run()
    print(result)
    if (result):
        launcher_state.set_state(launcher_state.LauncherState.LOADING)
        print(launcher_state.current_state)
        # app.application()
    else:
        launcher_state.set_state(launcher_state.LauncherState.PAUSED)
        print(launcher_state.current_state)
        # tray()          
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    startup_fn()
    sys.exit(app.exec())