This ensures the data is standardized and ready for analysis and future campaign imports.

## Project Features
- Splits the raw dataset into three logically grouped DataFrames:
  - `client.csv`: Contains client demographic and financial details.
  - `campaign.csv`: Stores campaign-related data, including contact details and outcomes.
  - `economics.csv`: Includes economic indicators linked to clients.
- Cleans and standardizes data columns to specified formats.
- Converts textual data to boolean or categorical values.
- Saves the processed data into separate CSV files.

## File Structure
├── bank_marketing.csv # Input raw dataset ├── client.csv # Processed client data ├── campaign.csv # Processed campaign data ├── economics.csv # Processed economic data ├── main.py # Main script for data cleaning and processing ├── README.md # Documentation

bash
Copy code

## Usage
1. Clone this repository to your local machine:
git clone https://github.com/your-username/bank-marketing-data-cleaning.git

markdown
Copy code
2. Install required libraries:
pip install pandas numpy

markdown
Copy code
3. Place the `bank_marketing.csv` file in the root directory.
4. Run the main script:
python main.py

perl
Copy code
5. Processed CSV files will be saved in the same directory:
- `client.csv`
- `campaign.csv`
- `economics.csv`

## Data Cleaning Details
- **`client.csv`**:
- Replaced periods (`.`) in "job" and "education" with underscores (`_`).
- Replaced "unknown" values in "education" with `NaN`.
- Converted "credit_default" and "mortgage" to boolean values.
- **`campaign.csv`**:
- Created a `last_contact_date` column from "day" and "month" columns.
- Converted campaign outcomes to boolean values.
- Dropped unnecessary columns like "month", "day", and "year".
- **`economics.csv`**:
- No specific cleaning required; retained as-is.

## Requirements
- Python 3.x
- pandas
- numpy

