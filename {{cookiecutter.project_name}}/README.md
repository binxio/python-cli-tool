# {{cookiecutter.project_name}}

TODO

## Initial setup

Before we can start we need to do some initial configuration. First we need to install all the dependencies. You can do this by executing the following command:

```bash
make install
```

You might have noticed that an initial commit was performed. This initial commit contains the starting point of the cookiecutter template plus the generated `pyproject.toml`.

Now it's time to configure your remote GitHub repository:

```bash
git remote add origin <REMOTE ADDRESS>
```

**Configuring the main branch**

Push the current `main` branch to the remote, using the following commands:

```bash
git branch -M main
git push -u origin main
```

**Configuring the develop branch**

Next, we will create a `develop` branch. You can use the following commands:

```bash
git checkout -b develop
git push --set-upstream origin develop
```

> Tip: You can now set the default branch to `develop`!

## Configure PyPi

To automatically upload release to [PyPi](https://pypi.org/) type the following command:

```bash
make release
```

You will be prompted for your username and password. After you created the initial release you can navigate to your [projects](https://pypi.org/manage/projects/). For your package, navigate to **Manage**, **Settings** and **Create a token for k8s-image-registry-secret**.

Pick an username and set the scope to the package you just created. Use the generated token to create a secret in GitHub.

On GitHub in your repository, go to **Settings**, **Security**, **Secrets** and then **Actions**. Here you will be able to create the repository secret.

Use `PYPI_API_TOKEN` as the name and the token from the previous step as the secret value.

## [Optional] Codecov.io

You can add the following to your `.github/workflows/ci.yml` file to enable [Codecov.io](https://app.codecov.io/)

{% raw %}```yaml
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v2
        with:
          fail_ci_if_error: true
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./reports/coverage.xml
      - name: Code Coverage Summary Report
        uses: irongut/CodeCoverageSummary@v1.1.0
        with:
          filename: reports/coverage.xml
          badge: true
          fail_below_min: true
          format: markdown
          output: both
          thresholds: 95 100
```{% endraw %}

**Configure Codecov.io**

Login to [codecov.io](https://app.codecov.io) locate your repository. Navigate to the **Settings** and then **General**. There you will find the `CODECOV_TOKEN` that you need to add to your GitHub repository.

Go to **Settings**, **Security**, **Secrets** and then **Actions**. Here you will be able to create the repository secret.

**Configure coverage report**

You will need to add the following to `test` target in the `Makefile`:

```Makefile
.PHONY: test
test: complexity-baseline ## Run the tests defined in the project
	pytest --junitxml=reports/pytest.xml --cov-report xml:reports/coverage.xml
```
