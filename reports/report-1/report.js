var reporting_data = {"lemoncheesecake_version": "1.3.1", "report_version": 1.1, "start_time": "2020-05-16T16:08:27.115Z", "end_time": "2020-05-16T16:08:28.027Z", "generation_time": "2020-05-16T16:08:28.049Z", "nb_threads": 1, "title": "Test Report", "info": [["Command line", "lcc run --tag tutorials, samples, equinix"]], "suites": [{"start_time": "2020-05-16T16:08:27.118Z", "end_time": "2020-05-16T16:08:28.027Z", "tests": [{"start_time": "2020-05-16T16:08:27.118Z", "end_time": "2020-05-16T16:08:28.027Z", "steps": [{"description": "test3", "start_time": "2020-05-16T16:08:27.118Z", "end_time": "2020-05-16T16:08:28.027Z", "entries": [{"type": "check", "description": "Expect http code to be equal to 200", "is_successful": false, "details": "Got 406", "time": "2020-05-16T16:08:28.017Z"}, {"type": "log", "level": "error", "message": "Caught unexpected exception while running test: Traceback (most recent call last):\n  File \"c:\\users\\atpc8\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\lemoncheesecake\\runner.py\", line 188, in run\n    self.test.callback(**test_func_params)\n  File \"C:\\Users\\atpc8\\sdlc\\lemontest\\suites\\firstsuite.py\", line 25, in test3\n    resp = r.json()\n  File \"c:\\users\\atpc8\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\requests\\models.py\", line 897, in json\n    return complexjson.loads(self.text, **kwargs)\n  File \"c:\\users\\atpc8\\appdata\\local\\programs\\python\\python37\\lib\\json\\__init__.py\", line 348, in loads\n    return _default_decoder.decode(s)\n  File \"c:\\users\\atpc8\\appdata\\local\\programs\\python\\python37\\lib\\json\\decoder.py\", line 337, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n  File \"c:\\users\\atpc8\\appdata\\local\\programs\\python\\python37\\lib\\json\\decoder.py\", line 355, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)\n", "time": "2020-05-16T16:08:28.027Z"}]}], "status": "failed", "status_details": null, "name": "test3", "description": "test3", "tags": ["equinix"], "properties": {}, "links": []}], "suites": [], "name": "firstsuite", "description": "my_suite", "tags": ["samples", "tutorials"], "properties": {}, "links": []}]}