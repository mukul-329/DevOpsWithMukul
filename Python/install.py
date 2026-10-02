
import platform
import subprocess
import sys


def install_package(package_name):
    # Detect the operating system
    os_name = platform.system()
    print(f"📦 Target detected: {os_name}")
    print(f"🔄 Attempting to install '{package_name}'...")

    try:
        if os_name == "Windows":
            # Windows: Uses Winget (built into modern Windows 10/11)
            # Use shell=True for Windows built-in commands
            subprocess.run(
                ["winget", "install", "-e", "--id", package_name], check=True
            )

        elif os_name == "Linux":
            # Linux: Assumes Debian/Ubuntu (APT). Needs sudo.
            print("🔑 This requires sudo privileges on Linux...")
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(
                ["sudo", "apt-get", "install", "-y", package_name], check=True
            )

        elif os_name == "Darwin":
            # macOS: Uses Homebrew (Brew)
            subprocess.run(["brew", "install", package_name], check=True)

        else:
            print(f"❌ Unsupported Operating System: {os_name}")
            sys.exit(1)

        print(f"✅ Successfully installed {package_name}!")

    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed. Error code: {e.returncode}")
    except FileNotFoundError:
        print(
            "❌ Missing package manager! Ensure winget (Windows) or brew (Mac) is installed."
        )


if __name__ == "__main__":
    # Change 'git' to the package identifier you actually want to install
    # Note: Package names might differ slightly across managers (e.g., Git.Git on Winget)
    TARGET_PACKAGE = "git"
    install_package(TARGET_PACKAGE)
