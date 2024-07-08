from litestar.testing import TestClient


def test_schema():
    # Test that health check and schema endpoints work from different root paths
    # Also confirms that there are no schema generation errors
    from test.app import app

    app.debug = True
    with TestClient(app=app) as test_client:
        resp = test_client.get("/schema")
        assert resp.status_code == 200, resp.text
