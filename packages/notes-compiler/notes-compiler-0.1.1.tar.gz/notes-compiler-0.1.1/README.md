# notes-compiler

## Usage

```bash
notes <input_path> <output_path>
```

For example:

```bash
notes ./src ./public
```

## Installation

While on the root of this repository:

```bash
poetry install
poetry build
cd dist
pip install notes_compiler-<VERSION>-py3-none-any.whl --force-reinstal
```

replacing `<VERSION` with the actual version number.
