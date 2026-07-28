
<h1>Data Engineering Pipeline for Electrolyzer Scale-Up: From Experimental Files to MySQL Database Intelligence</h1>

<p align="center">
    <img src="assest/s1.png" width="900" alt="ETL Pipeline Architecture">
</p>

<hr>

<h2>Phase 1 — Engineering Background: The Scale-Up Challenge</h2>

<h3>Supporting Electrolyzer Development Through Data Engineering</h3>

<p>Scaling an electrochemical electrolyzer from <strong>5 cm² laboratory-scale cells</strong> to <strong>25 cm² pilot-scale operation</strong> is not simply a matter of increasing reactor size. As the active area increases, complex engineering challenges emerge that directly influence reactor performance, efficiency, and long-term stability.</p>

<h4>Key scale-up challenges include:</h4>

<ul>
    <li>Catalyst composition and loading optimization</li>
    <li>Electrode and membrane selection</li>
    <li>Electrochemical performance validation</li>
    <li>Operating parameter optimization</li>
    <li>Reactor design evaluation</li>
    <li>Performance degradation monitoring</li>
    <li>Long-term operational stability assessment</li>
</ul>

<p>During experimental development, hundreds of electrochemical experiments were performed under different catalyst formulations, reactor configurations, and operating conditions.</p>

<p>Each experiment generated valuable information, including:</p>

<ul>
    <li>Catalyst properties</li>
    <li>Membrane characteristics</li>
    <li>Operating parameters</li>
    <li>Electrochemical measurements</li>
    <li>Methanol/ethanol production performance</li>
    <li>Stability and degradation behavior</li>
</ul>

<p>However, the experimental data existed across disconnected sources:</p>

<ul>
    <li>Excel laboratory spreadsheets</li>
    <li>CSV datasets</li>
    <li>Electrochemical testing software</li>
    <li>Sensor monitoring files</li>
    <li>Previous research records</li>
</ul>

<p>Before applying machine learning or advanced analytics, the first challenge was clear:</p>

<p><strong>How can experimental data generated during electrolyzer development be transformed into a reliable, centralized, and queryable engineering database?</strong></p>

<p>This question became the foundation of the data engineering workflow.</p>

<hr>

<h2>Phase 2 — Building the Electrolyzer Data Pipeline</h2>

<h3>The Data Challenge</h3>

<p>Experimental data were collected over multiple campaigns, but each dataset followed different structures and formats.</p>

<h4>Common issues included:</h4>

<h4>1. Inconsistent Naming</h4>

<p><strong>Before cleaning:</strong></p>

<ul>
    <li><code>CO2 Flow Rate</code></li>
    <li><code>CO₂_flow</code></li>
    <li><code>Gas Flow</code></li>
</ul>

<p><strong>After standardization:</strong></p>

<ul>
    <li><code>co2_flow_rate</code></li>
</ul>

<h4>2. Data Quality Issues</h4>

<p>The raw datasets contained:</p>

<ul>
    <li>Missing experimental values</li>
    <li>Duplicate measurements</li>
    <li>Different unit systems</li>
    <li>Mixed numerical and text formats</li>
    <li>Separated experimental metadata</li>
</ul>

<p>These issues made direct analysis inefficient because engineers had to manually search through multiple files before answering basic questions:</p>

<ul>
    <li>Which catalyst produced the highest yield?</li>
    <li>Which operating condition improved performance?</li>
    <li>How did performance change from 5 cm² to 25 cm²?</li>
    <li>Which experiments showed degradation?</li>
</ul>

<p>To solve this problem, an automated <strong>ETL (Extract, Transform, Load)</strong> pipeline was developed.</p>

<h3>ETL Architecture</h3>

<pre>
                 EXTRACT

    Excel Files    CSV Files    Sensor Data    Historical Records

                      ↓

                 TRANSFORM

    Data Cleaning    Data Wrangling    Missing Value Handling
    Duplicate Removal    Column Standardization
    Unit Conversion    Data Validation

                      ↓

                    LOAD

              MySQL Database

                      ↓

         SQL Analytics & Machine Learning
</pre>

<p><strong>Figure 1</strong> — Electrolyzer Experimental Data Pipeline</p>

<hr>

<h2>Phase 3 — Data Cleaning and Transformation</h2>

<p>Before storing data in MySQL, raw experimental datasets were processed using Python and Pandas. The objective was to convert inconsistent laboratory files into clean, structured datasets.</p>

<h3>1. Removing Duplicate Experiments</h3>

<p>Repeated experiments were identified and removed to prevent biased analysis.</p>

<pre>
df = df.drop_duplicates()
</pre>

<h3>2. Handling Missing Values</h3>

<p>Missing values were analyzed before database insertion.</p>

<pre>
df.isnull().sum()
</pre>

<p>Depending on the engineering importance, missing values were:</p>

<ul>
    <li>Removed</li>
    <li>Recovered from experimental records</li>
    <li>Replaced using statistical approaches</li>
</ul>

<h3>3. Standardizing Column Names</h3>

<p>Different experiments used different naming conventions.</p>

<p><strong>Before:</strong></p>

<ul>
    <li><code>Reaction Time (hour)</code></li>
    <li><code>Reaction_Time</code></li>
    <li><code>Time</code></li>
</ul>

<p><strong>After:</strong></p>

<ul>
    <li><code>reaction_time</code></li>
</ul>

<p><strong>Python transformation:</strong></p>

<pre>
# Clean column names
df.columns = (
    df.columns
    .str.strip()                      # remove leading/trailing spaces
    .str.replace(" ", "_")            # spaces → underscore
    .str.replace("%", "percent")      # % → percent
    .str.replace("µ", "micro")        # µ → micro
    .str.replace("²", "2")            # ² → 2
    .str.replace("/", "_", regex=False)
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace("-", "_"))

print(df.columns)
</pre>

<h3>4. Unit Standardization</h3>

<p>Engineering parameters were converted into consistent units:</p>

<ul>
    <li>Voltage (V)</li>
    <li>Current density (mA/cm²)</li>
    <li>Temperature (°C)</li>
    <li>Gas flow rate (sccm)</li>
    <li>Product concentration (µmol/mL)</li>
</ul>

<p>This ensured accurate comparison between experiments.</p>

<hr>

<h2>Phase 4 — Designing the MySQL Electrolyzer Database</h2>

<p>After cleaning and transformation, experimental data were transferred into a relational MySQL database. Instead of storing information in disconnected spreadsheets, the database created a structured data environment where experiments could be searched, compared, and analyzed efficiently.</p>

<h3>Database Architecture</h3>

<pre>
Electrolyzer_Database
│
├── experiments
│
├── catalyst_information
│
├── membrane_properties
│
├── operating_conditions
│
├── electrochemical_results
│
└── product_analysis
</pre>

<p><strong>Figure 2</strong> — MySQL Database Schema</p>

<h3>Creating Database and Tables</h3>

<p><strong>Database creation:</strong></p>

<pre>
CREATE DATABASE electrolyzer_db;
USE electrolyzer_db;
</pre>

<p><strong>Example experiment table:</strong></p>

<pre>
CREATE TABLE experiments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    catalyst_name VARCHAR(100),
    membrane_type VARCHAR(100),
    voltage FLOAT,
    current_density FLOAT,
    temperature FLOAT,
    reaction_time FLOAT,
    methanol_yield FLOAT,
    ethanol_yield FLOAT,
    degradation_rate FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
</pre>

<p>This structure allowed experimental information to be stored consistently and prepared for analytical queries.</p>

<hr>

<h2>Phase 5 — Python and MySQL Integration Using SQLAlchemy</h2>

<p>To automate communication between Python data workflows and MySQL, SQLAlchemy was used as the database connection layer. The goal was to create a repeatable pipeline where new experimental files could automatically flow into the database.</p>

<h3>Database Connection</h3>

<pre>
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://username:password@localhost/electrolyzer_db")
</pre>

<h3>Loading Clean Experimental Data</h3>

<p>After preprocessing:</p>

<pre>
df.to_sql(
    "experiments",
    con=engine,
    if_exists="append",
    index=False)
</pre>

<p>This enabled:</p>

<ul>
    <li>✅ Automated data ingestion</li>
    <li>✅ Reproducible ETL workflow</li>
    <li>✅ Python–SQL integration</li>
    <li>✅ Scalable experimental data storage</li>
</ul>

<h3>Automated Excel-to-MySQL ETL Workflow</h3>

<p>The final pipeline allowed researchers to add new experimental files without manually rebuilding datasets.</p>

<p><strong>Workflow:</strong></p>

<pre>
New Excel Experiment File
          ↓
Python ETL Script
          ↓
Cleaning + Transformation
          ↓
MySQL experiments Table
          ↓
SQL Query Analytics
</pre>

<p><strong>Example:</strong></p>

<pre>
def append_excel_to_mysql(file_path):
    df = pd.read_excel(file_path)
    df = df.dropna()
    df.to_sql(
        "experiments",
        engine,
        if_exists="append",
        index=False
    )
</pre>

<hr>

<h2>Phase 6 — SQL-Based Electrolyzer Performance Analytics</h2>

<p>Once experimental data were centralized in MySQL, SQL became the main tool for extracting engineering insights. Instead of manually reviewing hundreds of spreadsheets, engineers could answer performance questions instantly.</p>

<hr>

<h3>Query 1: Database Validation and Experimental Data Access</h3>

<p><strong>SQL Query:</strong></p>

<pre>
SELECT * FROM preprocessed;
</pre>

<p><strong>Engineering Question:</strong><br>
What experimental records are available after preprocessing, and can the cleaned electrolyzer dataset be successfully accessed from the database?</p>

<p><strong>Purpose:</strong></p>

<ul>
    <li>Verify successful ETL loading</li>
    <li>Inspect processed experimental data</li>
    <li>Confirm database connectivity</li>
    <li>Validate data structure before analysis</li>
</ul>

<hr>

<h3>Query 2: Missing Data Investigation</h3>

<p><strong>SQL Query — Identify Missing Voltage Measurements:</strong></p>

<pre>
SELECT * 
FROM preprocessed 
WHERE voltage IS NULL;
</pre>

<p><strong>Engineering Question:</strong><br>
Which electrolyzer experiments are missing voltage measurements?</p>

<p><strong>Purpose:</strong></p>

<ul>
    <li>Identify incomplete experimental records</li>
    <li>Detect sensor or data acquisition problems</li>
    <li>Evaluate data quality before ML modeling</li>
</ul>

<p><strong>SQL Query — Valid Voltage Measurements:</strong></p>

<pre>
SELECT * 
FROM preprocessed 
WHERE voltage IS NOT NULL;
</pre>

<p><strong>Engineering Question:</strong><br>
Which experiments contain valid voltage measurements?</p>

<p><strong>SQL Query — Handling Missing Values:</strong></p>

<pre>
UPDATE preprocessed 
SET voltage = 0 
WHERE voltage IS NULL;
</pre>

<p><strong>Note:</strong> For ML, median imputation was considered instead of replacing with zero.</p>

<hr>

<h3>Query 3: Electrolyzer Productivity Analysis</h3>

<p><strong>SQL Query:</strong></p>

<pre>
SELECT 
    cathod_catalyst,
    Methanol_Yield_micromol_ml_ / Reaction_Time_hr AS efficiency 
FROM preprocessed;
</pre>

<p><strong>Engineering Question:</strong><br>
Which cathode catalyst provides the highest methanol productivity per unit reaction time?</p>

<p><strong>Calculated Metric:</strong></p>

<pre>
Methanol Productivity = Methanol Yield / Reaction Time
</pre>

<p><strong>Purpose:</strong></p>

<ul>
    <li>Compare catalyst performance</li>
    <li>Normalize production by experiment duration</li>
    <li>Identify high-efficiency catalyst candidates</li>
</ul>

<p><strong>Example Output:</strong></p>

<table border="1" cellpadding="5">
    <tr>
        <th>Catalyst</th>
        <th>Efficiency (µmol/mL/hr)</th>
    </tr>
    <tr>
        <td>Pt-Co</td>
        <td>25.4</td>
    </tr>
    <tr>
        <td>Ni</td>
        <td>18.2</td>
    </tr>
    <tr>
        <td>Co</td>
        <td>12.5</td>
    </tr>
</table>

<hr>

<h3>Query 4: Catalyst Composition Analysis</h3>

<p><strong>SQL Query:</strong></p>

<pre>
SELECT
    process_type,
    AVG(Pt_atpercent_in_metal_element) AS avg_pt,
    AVG(Ni_atpercent_in_metal_element) AS avg_ni,
    AVG(Co_atpercent_in_metal_element) AS avg_co
FROM preprocessed
GROUP BY process_type;
</pre>

<p><strong>Engineering Question:</strong><br>
How does catalyst metal composition vary across different electrochemical processes?</p>

<p><strong>Purpose:</strong></p>

<ul>
    <li>Compare catalyst formulations</li>
    <li>Understand metal loading distribution</li>
    <li>Identify relationships between composition and performance</li>
</ul>

<p><strong>Example Output:</strong></p>

<table border="1" cellpadding="5">
    <tr>
        <th>Process</th>
        <th>Pt %</th>
        <th>Ni %</th>
        <th>Co %</th>
    </tr>
    <tr>
        <td>CO₂ reduction</td>
        <td>30</td>
        <td>20</td>
        <td>50</td>
    </tr>
    <tr>
        <td>CH₄ conversion</td>
        <td>45</td>
        <td>10</td>
        <td>45</td>
    </tr>
</table>

<hr>

<h3>Query 5: Duplicate Experimental Condition Detection</h3>

<p><strong>SQL Query:</strong></p>

<pre>
SELECT 
    cathod_catalyst,
    anode_catalyst,
    Voltage_V,
    CH4_Flow_rate_sscm,
    COUNT(*) AS duplicates
FROM preprocessed
GROUP BY 
    cathod_catalyst,
    anode_catalyst,
    Voltage_V,
    CH4_Flow_rate_sscm
HAVING COUNT(*) > 1;
</pre>

<p><strong>Engineering Question:</strong><br>
Are there repeated experiments performed under identical catalyst and operating conditions?</p>

<p><strong>Purpose:</strong></p>

<ul>
    <li>Detect duplicate experiments</li>
    <li>Prevent biased ML training</li>
    <li>Verify experimental reproducibility</li>
    <li>Identify repeated validation tests</li>
</ul>

<p><strong>Example Output:</strong></p>

<table border="1" cellpadding="5">
    <tr>
        <th>Cathode</th>
        <th>Anode</th>
        <th>Voltage</th>
        <th>CH₄ Flow</th>
        <th>Count</th>
    </tr>
    <tr>
        <td>Pt-Co</td>
        <td>IrO₂</td>
        <td>3V</td>
        <td>20 sccm</td>
        <td>3</td>
    </tr>
</table>

<p><strong>Interpretation:</strong><br>
Three experiments were performed under identical conditions, indicating possible replication experiments or duplicate records.</p>

<hr>

<h3>Query 6: Average Yield per Catalyst Combination</h3>

<p><strong>SQL Query:</strong></p>

<pre>
SELECT 
    cathod_catalyst,
    anode_catalyst,
    AVG(Methanol_Yield_micromol_ml_) AS avg_yield,
    COUNT(*) AS experiment_count
FROM preprocessed
GROUP BY cathod_catalyst, anode_catalyst
ORDER BY avg_yield DESC;
</pre>

<p><strong>Engineering Question:</strong><br>
Which catalyst combination produces the highest average methanol yield?</p>

<p><strong>Python Implementation:</strong></p>

<pre>
df = pd.read_sql(sql, engine)
df.head()
</pre>

<p align="center">
    <img src="assest/S3.png" width="900" alt="Average Yield Results">
</p>

<hr>

<h3>Query 7: Yield Efficiency (Yield per Reaction Time)</h3>

<p><strong>SQL Query:</strong></p>

<pre>
SELECT 
    cathod_catalyst,
    Methanol_Yield_micromol_ml_ / Reaction_Time_hr AS efficiency 
FROM preprocessed;
</pre>

<p><strong>Engineering Question:</strong><br>
How does methanol yield efficiency compare across different catalysts when normalized by reaction time?</p>

<p><strong>Python Implementation:</strong></p>

<pre>
df = pd.read_sql(sql, engine)
df.head()
</pre>

<p align="center">
    <img src="assest/S2.png" width="900" alt="Efficiency Results">
</p>

<hr>

<h3>Query 8: Performance Comparison — 5 cm² vs 25 cm²</h3>

<p><strong>SQL Query:</strong></p>

<pre>
SELECT 
    electrode_area,
    AVG(methanol_yield) AS avg_methanol,
    AVG(ethanol_yield) AS avg_ethanol,
    AVG(faradaic_efficiency) AS avg_efficiency
FROM preprocessed
GROUP BY electrode_area
ORDER BY electrode_area;
</pre>

<p><strong>Engineering Question:</strong><br>
How does electrolyzer performance change when scaling from 5 cm² to 25 cm²?</p>

<p><strong>Purpose:</strong></p>

<ul>
    <li>Quantify scale-up performance loss</li>
    <li>Identify area-dependent effects</li>
    <li>Guide reactor design improvements</li>
</ul>

<hr>

<h3>Query 9: Degradation Trend Analysis</h3>

<p><strong>SQL Query:</strong></p>

<pre>
SELECT 
    catalyst_name,
    reaction_time,
    voltage,
    degradation_rate,
    CASE 
        WHEN degradation_rate < 0.01 THEN 'Stable'
        WHEN degradation_rate < 0.05 THEN 'Moderate'
        ELSE 'Severe'
    END AS degradation_category
FROM preprocessed
WHERE reaction_time > 10
ORDER BY degradation_rate DESC;
</pre>

<p><strong>Engineering Question:</strong><br>
Which catalysts show the highest degradation rates during long-term operation?</p>

<p><strong>Purpose:</strong></p>

<ul>
    <li>Identify degradation-prone catalysts</li>
    <li>Establish stability benchmarks</li>
    <li>Support catalyst lifetime predictions</li>
</ul>

<hr>



<p><strong>Engineering Question:</strong><br>
What combination of temperature and current density yields the highest methanol production under optimal voltage conditions?</p>

<p><strong>Purpose:</strong></p>

<ul>
    <li>Identify optimal operating windows</li>
    <li>Guide experimental design</li>
    <li>Support scale-up parameter selection</li>
</ul>

<hr>

<h2>Engineering Impact: From Experimental Data to Decision Intelligence</h2>

<p>By transforming fragmented laboratory files into a structured MySQL database, this project created the foundation for advanced analytics and machine learning.</p>

<p>The SQL-based data engineering framework enabled:</p>

<ul>
    <li>✅ Centralized electrolyzer experimental database</li>
    <li>✅ Automated Excel/CSV data ingestion</li>
    <li>✅ Data cleaning and validation pipeline</li>
    <li>✅ Python–MySQL integration using SQLAlchemy</li>
    <li>✅ Fast experimental querying</li>
    <li>✅ Reproducible engineering analysis</li>
    <li>✅ Preparation of clean datasets for machine learning models</li>
</ul>

<p><strong>Business Impact Summary:</strong></p>

<table border="1" cellpadding="5">
    <tr>
        <th>Metric</th>
        <th>Before</th>
        <th>After</th>
        <th>Improvement</th>
    </tr>
    <tr>
        <td>Data Query Time</td>
        <td>Hours to Days</td>
        <td>Seconds</td>
        <td>99.9%</td>
    </tr>
    <tr>
        <td>Data Processing</td>
        <td>Manual</td>
        <td>Automated</td>
        <td>100%</td>
    </tr>
    <tr>
        <td>Experiment Comparison</td>
        <td>Difficult</td>
        <td>Instant</td>
        <td>Significant</td>
    </tr>
    <tr>
        <td>Data Consistency</td>
        <td>Inconsistent</td>
        <td>Standardized</td>
        <td>Complete</td>
    </tr>
</table>

<hr>

<p><em>End of Document — Data Engineering Pipeline for Electrolyzer Scale-Up</em></p>

</body>
</html>
