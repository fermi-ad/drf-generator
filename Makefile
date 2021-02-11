drf_generator.tgz : LICENSE README.md setup.py drf_generator/*py
	tar czf $@ $^

clean ::
	find . -type f -name '*~' -delete
	for ii in $$(find . -type d -name __pycache__); do \
	  rm -rf $${ii}; \
	done
	rm -rf acsys.tgz __pycache__
