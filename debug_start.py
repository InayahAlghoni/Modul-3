import sys, atexit, inspect, traceback

atexit.register(lambda: print("[x] proses berakhir"))
print("[1] Python", sys.version.split()[0])

try:
    import customtkinter as ctk
    print("[2] customtkinter", ctk.__version__)

    import controllers.auth_controller as ac
    import views.login_view as lv
    print("[3] auth_controller :", ac.__file__)
    print("    login_view      :", lv.__file__)
    print("    login_view punya btn_register:", "btn_register" in inspect.getsource(lv))

    app = ac.AuthController()
    print("[4] AuthController dibuat | koneksi DB:", "ADA" if app.model.conn else "TIDAK ADA")

    app.view.after(500, lambda: print("[5] mainloop berjalan | jendela ada:", bool(app.view.winfo_exists())))
    app.run()
    print("[6] mainloop selesai")
except Exception:
    traceback.print_exc()