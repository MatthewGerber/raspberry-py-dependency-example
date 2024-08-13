# raspberry-py-dependency-example
An example of consuming [raspberry-py](https://pypi.org/project/raspberry-py/) via PyPI dependency.

# Installation
1. Clone this repository locally to a Raspberry Pi.
2. From the local repository directory:
   ```shell
   poetry env use 3.11
   poetry install
   ```
3. Build the circuit referenced in `src/raspberry_pi_dependency_example/breathing_led.py`.
4. Run the script:  
   ```shell
   poetry run python src/raspberry_pi_dependency_example/breathing_led.py
   ```