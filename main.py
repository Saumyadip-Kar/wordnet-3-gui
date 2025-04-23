import subprocess
import webbrowser
import time

def run_servers():
    # Start the backend server
    backend = subprocess.Popen(["python3", "-m", "backend"]) #Use python instead of python3 for windows

    # Start the frontend server
    frontend = subprocess.Popen(["python3", "-m", "http.server", "4000"]) #Use python instead of python3 for windows

    # Wait briefly to ensure servers have time to start
    # time.sleep(2)

    # Open the frontend in the default browser
    webbrowser.open("http://localhost:4000")

    try:
        # Wait for both processes to complete (they won’t unless terminated)
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("Shutting down servers...")
        backend.terminate()
        frontend.terminate()

if __name__ == "__main__":
    run_servers()
