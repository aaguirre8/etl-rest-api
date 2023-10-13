import argparse
from setuptools import setup

def create_wheel():
    setup(
        name="orion_digital_twin_app",
        version=0.1,
        packages=["src"],
    )
    print("Successfully created whl file in dist/")

# def main():
#     parser = argparse.ArgumentParser(description="Create a .whl file for Orion Digital Twin App")
#     parser.add_argument("--version", type=str, required=True, help="Version of the package")
#     args = parser.parse_args()

#     create_wheel(args.version)

if __name__ == "__main__":
    create_wheel()
