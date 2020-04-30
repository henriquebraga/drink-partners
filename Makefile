clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.cache" -type d | xargs rm -rf
	@find . -name "*htmlcov" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f coverage.xml

requirements-test:
	@pip install -r requirements/test.txt

requirements-dev:
	@pip install -r requirements/dev.txt

test:
	@SIMPLE_SETTINGS=drink_partners.settings.test py.test -xs -vv drink_partners

test-matching:
	@SIMPLE_SETTINGS=drink_partners.settings.test py.test -rxs --pdb -k$(Q) drink_partners

test-coverage:
	@SIMPLE_SETTINGS=drink_partners.settings.test pytest --cov=drink_partners drink_partners --cov-report term-missing --cov-report xml

lint:
	@flake8
	@isort --check

run:
	@gunicorn drink_partners:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS=drink_partners.settings.development

detect-outdated-dependencies:
	@sh -c 'output=$$(pip list --outdated); echo "$$output"; test -z "$$output"'

release-patch: ## Create patch release
	bump2version patch --dry-run --no-tag --no-commit --list | grep new_version= | SIMPLE_SETTINGS=drink_partners.settings.test sed -e 's/new_version=//' | xargs -n 1 towncrier --yes --version
	git commit -am 'Update CHANGELOG'
	bump2version patch

release-minor: ## Create minor release
	bump2version minor --dry-run --no-tag --no-commit --list | grep new_version= | sed -e 's/new_version=//' | SIMPLE_SETTINGS=drink_partners.settings.test xargs -n 1 towncrier --yes --version
	git commit -am 'Update CHANGELOG'
	bump2version minor

release-major: ## Create major release
	bump2version major --dry-run --no-tag --no-commit --list | grep new_version= | sed -e 's/new_version=//' | SIMPLE_SETTINGS=drink_partners.settings.test xargs -n 1 towncrier --yes --version
	git commit -am 'Update CHANGELOG'
	bump2version major

check-vulnerabilities:
	safety check -r requirements/base.txt
