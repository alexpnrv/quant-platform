import subprocess

def test_cli_help():
    result = subprocess.run(["python", "-m", "quant_platform.api.cli", "--help"], capture_output=True)
    assert "Quant Platform CLI" in result.stdout.decode("utf-8")