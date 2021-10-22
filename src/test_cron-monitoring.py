from unittest.mock import MagicMock, patch
import pytest
import json 

from core.job_manager import JobManager
from tests.mock import SUBPROCESS_MOCK

job_manager = JobManager()

@patch("core.job_manager.subprocess.run")
def test_get_list_of_single_jobs(mock_run):
    mock_stdout = MagicMock()
    mock_stdout.configure_mock(
        **{
            "stdout.decode.return_value": SUBPROCESS_MOCK["SINGLE_JOB"]
        }
    )

    mock_run.return_value = mock_stdout
    jobs = job_manager.get_jobs()

    assert len(jobs) == 1
    assert jobs[0].id == SUBPROCESS_MOCK["SINGLE_JOB_ID"]

@patch("core.job_manager.subprocess.run")
def test_get_list_of_empty_jobs(mock_run):
    mock_stdout = MagicMock()
    mock_stdout.configure_mock(
        **{
            "stdout.decode.return_value": ""
        }
    )

    mock_run.return_value = mock_stdout
    jobs = job_manager.get_jobs()

    assert len(jobs) == 0

@patch("core.job_manager.subprocess.run")
def test_add_job(mock_run):
    mock_stdout = MagicMock()
    mock_stdout.configure_mock(
        **{
            "stdout.decode.return_value": ""
        }
    )

    mock_run.return_value = mock_stdout

    try:
        job_manager.add_job(
            "*","*","*","*","*","/","python3","/","2>&1"
        )
        # Adding a new job must complete successfully
        assert True
    except:
        # Any error on the creation of job must result into false assertion.
        assert False

    try:
        job_manager.add_job()
        # Adding an empty job must result into false assertion.
        assert False
    except:
        # Any error on the creation of job must result into false assertion.
        assert True
