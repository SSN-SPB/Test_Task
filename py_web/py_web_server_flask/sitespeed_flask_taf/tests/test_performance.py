from utils.sitespeed_runner import run_sitespeed


def test_flask_homepage_performance():
    result = run_sitespeed(
        "http://127.0.0.1:5000/",
        report_name="homepage",
    )

    print(result.stdout)
    print(result.stderr)

    assert result.returncode == 0, (
        "Sitespeed execution failed.\n\n"
        f"STDOUT:\n{result.stdout}\n\n"
        f"STDERR:\n{result.stderr}"
    )
