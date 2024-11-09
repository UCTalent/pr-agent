
# Generated by CodiumAI
import pytest

from pr_agent.algo.utils import try_fix_yaml


class TestTryFixYaml:

    # The function successfully parses a valid YAML string.
    def test_valid_yaml(self):
        review_text = "key: value\n"
        expected_output = {"key": "value"}
        assert try_fix_yaml(review_text) == expected_output

    # The function adds '|-' to 'relevant line:' if it is not already present and successfully parses the YAML string.
    def test_add_relevant_line(self):
        review_text = "relevant line: value: 3\n"
        expected_output = {'relevant line': 'value: 3\n'}
        assert try_fix_yaml(review_text) == expected_output

    # The function extracts YAML snippet
    def test_extract_snippet(self):
        review_text = '''\
Here is the answer in YAML format:

```yaml
name: John Smith
age: 35
```
'''
        expected_output = {'name': 'John Smith', 'age': 35}
        assert try_fix_yaml(review_text) == expected_output

    # The function removes the last line(s) of the YAML string and successfully parses the YAML string.
    def test_remove_last_line(self):
        review_text = "key: value\nextra invalid line\n"
        expected_output = {"key": "value"}
        assert try_fix_yaml(review_text) == expected_output

    # The YAML string is empty.
    def test_empty_yaml_fixed(self):
        review_text = ""
        assert try_fix_yaml(review_text) is None


    # The function extracts YAML snippet
    def test_no_initial_yaml(self):
        review_text = '''\
I suggest the following:

code_suggestions:
- relevant_file: |
    src/index.ts
  label: |
    best practice

- relevant_file: |
    src/index2.ts
  label: |
    enhancment
```

We can further improve the code by using the `const` keyword instead of `var` in the `src/index.ts` file.
'''
        expected_output = {'code_suggestions': [{'relevant_file': 'src/index.ts\n', 'label': 'best practice\n'}, {'relevant_file': 'src/index2.ts\n', 'label': 'enhancment'}]}

        assert try_fix_yaml(review_text, first_key='code_suggestions', last_key='label') == expected_output

    def test_with_initial_yaml(self):
        review_text = '''\
I suggest the following:

```
code_suggestions:
- relevant_file: |
    src/index.ts
  label: |
    best practice

- relevant_file: |
    src/index2.ts
  label: |
    enhancment
```

We can further improve the code by using the `const` keyword instead of `var` in the `src/index.ts` file.
'''
        expected_output = {'code_suggestions': [{'relevant_file': 'src/index.ts\n', 'label': 'best practice\n'}, {'relevant_file': 'src/index2.ts\n', 'label': 'enhancment'}]}
        assert try_fix_yaml(review_text, first_key='code_suggestions', last_key='label') == expected_output
