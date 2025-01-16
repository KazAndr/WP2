# README for DM-Time Dataset Processor

## Overview

The `DMTimeDataSetCreator` is a Python-based tool designed to process filterbank file of an observations and based on transient list of candidates form [TransientX](https://github.com/ypmen/TransientX) create an augmented **DM-Time Dataset**. This dataset is used for analyzing transient signals, such as pulsars or fast radio bursts (FRBs), by generating time-series images across different **Dispersion Measure (DM)** values.

---

## Directory Structure

```
├── processor.py          # Main script containing the `DMTimeDataSetCreator` class and its methods
├── config.json           # Configuration file with paths and parameters for processing
├── module_usage.ipynb    # Jupyter Notebook example of how to use the processor
```

---

## Dependencies

The processor relies on the following libraries:
- `numpy`
- `pandas`
- `glob`
- `json`
- `os`
- `decimal`
- `tqdm` (for progress bars)
- `your` (library for handling filterbank files)

Install these dependencies using `pip`:

```bash
pip install numpy pandas tqdm your
```

---

## Configuration File (`config.json`)

This file defines the paths and parameters required for processing. Below is an explanation of each field:

- **filterbank_path**: Path to the `.fil` file containing filterbank data.
- **transientx_time_series_path**: Directory containing `.dat` files for time series at different DM values.
- **transientx_candidates_path**: Path to the file listing transient candidates.
- **ntsamples**: Number of time samples to extract for each candidate.
- **dm_ranges**: A dictionary specifying the DM range for pulses.

### Example (`config.json`)

```json
{
  "filterbank_path": "data/filterbank_files/B0531+21_59000_48386.fil",
  "transientx_time_series_path": "data/transientx/time_series/",
  "transientx_candidates_path": "data/transientx/B0531+21_59000.4838657407_cfbf00000.cands",
  "ntsamples": 256,
  "dm_ranges": {
    "pulses": [56, 58]
  }
}
```

---

## Processor Implementation (`processor.py`)

The `DMTimeDataSetCreator` class provides the following key functionalities:

### Methods:

1. **`__init__(config_path)`**
   - Loads the configuration file and initializes attributes.

2. **`process()`**
   - Main method to:
     - Load and categorize candidates.
     - Generate DM-Time images for pulses, zero DM events, and the "rest" category.
     - Combine datasets and save them as `.npy` files.

3. **`normalize_image_to_255(image)`**
   - Normalizes a 2D image to a range of 0-255.

4. **`_create_dm_time_image()`**
   - Creates a DM-Time image from the list of `.dat` files.

5. **`_get_position_in_filfile(mjd_pulse)`**
   - Maps an MJD pulse to its corresponding position in the filterbank file.

6. **`_process_candidates(candidates, label, exclude_positions=None, target_count=None)`**
   - Extracts time-series segments for pulses, zero DM events, or random segments for the "rest" category.

7. **`_generate_exclude_positions(pulse_candidates, zero_dm_events)`**
   - Generates a list of positions to exclude when processing the "rest" category.

### Outputs:
The processor saves:
- Combined dataset: `<output_dir>/<dataset_name>_DM_time_dataset_realbased.npy`
- Corresponding labels: `<output_dir>/<dataset_name>_DM_time_dataset_realbased_labels.npy`

---

## Example Usage (`module_usage.ipynb`)

An example Jupyter Notebook demonstrates how to use the `DMTimeDataSetCreator`:

```python
from processor import DMTimeDataSetCreator

# Specify the path to the configuration file
config_path = "config.json"

# Initialize the processor
processor = DMTimeDataSetCreator(config_path)

# Process the data and generate outputs
processor.process()
```

Run this notebook to process the transient candidates and create the dataset.

---

## Output Description

The processor creates:
1. **DM-Time Dataset (`.npy`)**:
   - A 3D array where each sample is a time-series image across different DM values.

2. **Labels (`.npy`)**:
   - A corresponding label array indicating the class of each sample:
     - `'Pulse'` for true signals.
     - `'Artefact'` for zero DM events and the rest of the events.

---

## Notes

- Ensure the paths in `config.json` are valid and accessible.
- The processor expects `.dat` files in `transientx_time_series_path` and a valid `.cands` file at `transientx_candidates_path`.
- For best performance, use high-quality input data and adjust parameters in `config.json` as needed.
