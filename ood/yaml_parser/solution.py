import yaml


if __name__ == "__main__":
    # The main idea: install pyyaml, do yaml.safe_load(file) => work with dict
    with open('example.yml', 'r') as file:
        prime_service = yaml.safe_load(file)
