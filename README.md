
<h1 align="center">Machine Learning-Driven Optimization of Methane Electrolysis</h1>
<h2 align="center">Scaling Electrochemical Conversion from 5 cm² to 25 cm² for Sustainable Methanol and Ethanol Production</h2>

<p align="center">
    <img src="assest/1.png" width="900" alt="Project Architecture Overview">
</p>


<hr>

<h2 id="story"> The Story Behind This Project</h2>


<p><strong>Imagine this:</strong> You're an electrochemical engineer who has spent three years developing a promising technology — converting methane into methanol and ethanol using electricity. Your 5 cm² laboratory cells show incredible results. The data looks promising. Funding is secured for scale-up.</p>

<p>Then reality hits.</p>

<p>Scaling to 25 cm² introduces challenges you never saw coming:</p>
<ul>
    <li> Performance drops unexpectedly</li>
    <li> Product selectivity shifts unpredictably</li>
    <li> Degradation appears without warning</li>
    <li> Results become inconsistent</li>
</ul>

<p><strong>But the real nightmare? The data.</strong></p>

<p>Your experimental data is scattered across:</p>
<ul>
    <li> <strong>23 Excel spreadsheets</strong> — each with different column names</li>
    <li> <strong>CSV files</strong> — in various formats and structures</li>
    <li> <strong>Electrochemical testing logs</strong> — proprietary software exports</li>
    <li> <strong>Historical lab reports</strong> — PDFs, Word docs, and handwritten notes</li>
    <li> <strong>Sensor data files</strong> — different sampling rates and formats</li>
</ul>

<p><strong>The same parameter has different names everywhere:</strong></p>
<table border="1" cellpadding="5">
    <tr>
        <th>Parameter</th>
        <th>Name in File 1</th>
        <th>Name in File 2</th>
        <th>Name in File 3</th>
    </tr>
    <tr>
        <td>CO₂ Flow Rate</td>
        <td><code>CO2 Flow Rate</code></td>
        <td><code>CO₂_flow</code></td>
        <td><code>Gas Rate</code></td>
    </tr>
    <tr>
        <td>Reaction Time</td>
        <td><code>Reaction Time (h)</code></td>
        <td><code>Reaction_Time</code></td>
        <td><code>Time</code></td>
    </tr>
    <tr>
        <td>Temperature</td>
        <td><code>Temp °C</code></td>
        <td><code>Temperature</code></td>
        <td><code>T</code></td>
    </tr>
</table>

<p><strong>The human cost:</strong></p>
<ul>
    <li> Days spent manually comparing spreadsheets and results</li>
    <li>Hidden relationships remain invisible</li>
    <li>Early degradation signs go unnoticed</li>
    <li> Epensive experiments repeated unnecessarily</li>
    <li> Scale-up decisions based on incomplete data</li>
</ul>

<p><strong>This is the reality of traditional electrochemical research.</strong> And it's exactly what this project was built to solve.</p>

<hr>

<h2 id="problem"> The Problem </h2>

<h3>Technical Challenges: From 5 cm² to 25 cm²</h3>

<p>Scaling an electrochemical reactor isn't just about making things bigger — it's about solving entirely new engineering challenges:</p>

<table border="1" cellpadding="5">
    <tr>
        <th>Challenge</th>
        <th>Description</th>
        <th>Impact</th>
    </tr>
    <tr>
        <td> Mass Transport</td>
        <td>Reactants don't reach electrodes uniformly</td>
        <td>Lower conversion rates</td>
    </tr>
    <tr>
     <td>Increase Surface Area</td>
     <td>Difficulty maintaining uniform catalyst utilization and reactant distribution</td>
     <td>Lower electrochemical performance and reduced conversion efficiency</td>
    </tr>
    <tr>
        <td> Current Distribution</td>
        <td>Non-uniform current across larger area</td>
        <td>Performance losses</td>
    </tr>
    <tr>
        <td> Catalyst Utilization</td>
        <td>Deactivation mechanisms become more pronounced</td>
        <td>Shorter operational life</td>
    </tr>
    <tr>
        <td> Membrane Stability</td>
        <td>Degradation accelerates with size</td>
        <td>Performance decline</td>
    </tr>
    <tr>
        <td> Product Selectivity</td>
        <td>Methanol vs. ethanol ratio shifts</td>
        <td>Product quality issues</td>
    </tr>
</table>

<h3>Data Challenges: The Hidden Enemy</h3>

<table border="1" cellpadding="5">
    <tr>
        <th>Data Issue</th>
        <th>Magnitude</th>
        <th>Consequence</th>
    </tr>
    <tr>
        <td>❌ Inconsistent Naming</td>
        <td>47+ different column names</td>
        <td>Manual mapping required</td>
    </tr>
    <tr>
        <td>❌ Missing Values</td>
        <td>~15% of data missing</td>
        <td>Incomplete analysis</td>
    </tr>
    <tr>
        <td>❌ Duplicate Records</td>
        <td>127 duplicate experiments</td>
        <td>Biased results</td>
    </tr>
    <tr>
        <td>❌ Mixed Units</td>
        <td>12 different unit systems</td>
        <td>Comparison errors</td>
    </tr>
    <tr>
        <td>❌ Fragmented Storage</td>
        <td>23+ different files</td>
        <td>Days to query data</td>
    </tr>
</table>

<h3>The Research Questions We Couldn't Answer</h3>
<ul>
    <li> Which catalyst produced the highest yield across all experiments?</li>
    <li> How did performance change when scaling from 5 cm² to 25 cm²?</li>
    <li> Which operating conditions maximized methanol production?</li>
    <li> What caused the unexpected degradation in long-term tests?</li>
    <li> Which experiments showed statistically significant results?</li>
</ul>

<p><strong>This is the problem we set out to solve.</strong></p>

<hr>

<h2 id="solution"> Our Solution</h2>

<h3>A Digital Intelligence Layer for Electrochemical Engineering</h3>

<p>We built an end-to-end <strong>Data Engineering, Machine Learning, and Decision Intelligence platform</strong> that transforms fragmented experimental data into actionable engineering insights.</p>

<h4>What I Built:</h4>

<ol>
    <li><strong> Data Engineering Foundation</strong>
        <ul>
            <li>Automated ETL pipeline from Excel/CSV to MySQL</li>
            <li>Data cleaning, validation, and standardization</li>
            <li>Centralized experimental database with 6 interconnected tables</li>
        </ul>
    </li>
    <li><strong> DataBase Analytics & Insights</strong>
        <ul>
            <li>Creating the relational database (MySQL) to gather all Experimental Data </li>
            <li>Using SQLAlchemy for connecting dataset with new data (excell, CSV etc)</li>
            <li>SQL-based performance analytics</li>
            <li>Exploratory Data Analysis (EDA)</li>
            <li>Statistical analysis (ANOVA, Correlation, Hypothesis Testing)</li>
        </ul>
    </li>
    <li><strong> Machine Learning for Catalyst Design & Production Prediction</strong>
    <ul>
        <li>Predict methanol and ethanol production using ML models (R² > 0.91)</li>
        <li>Catalyst performance ranking and selection</li>
        <li>Feature importance analysis and SHAP interpretation</li>
    </ul>
</li>

<li><strong> Machine Learning for Electrolyzer Process Optimization & Scale-Up</strong>
    <ul>
        <li>Bayesian optimization of operating conditions</li>
        <li>Optimization of voltage, current density, temperature, and reaction time</li>
        <li>Design-space exploration for scaling from 5 cm² to 25 cm² electrolyzers</li>
    </ul>
</li>

<li><strong> Machine Learning for Predictive Maintenance & Failure Risk</strong>
    <ul>
        <li>Failure risk classification (Normal / Warning / Critical)</li>
        <li>Predictive maintenance and degradation monitoring</li>
        <li>Remaining Useful Life (RUL) estimation and early fault detection</li>
    </ul>
</li>
    <li><strong> Procurement Intelligence</strong>
        <ul>
            <li>Automated web scraping of material prices</li>
            <li>ARIMA time-series forecasting</li>
            <li>Data-driven procurement recommendations</li>
            <li>Creating the relational database (SQLite)</li>
        </ul>
    </li>
    <li><strong> Unified Dashboard</strong>
        <ul>
            <li>Streamlit-based interactive platform</li>
            <li>Real-time monitoring & visualization</li>
            <li>Decision support for engineers</li>
        </ul>
    </li>
</ol>

<h4>What This Enables:</h4>

<table border="1" cellpadding="5">
    <tr>
        <th>Capability</th>
        <th>Before</th>
        <th>After</th>
    </tr>
    <tr>
        <td>Query experimental data</td>
        <td>Hours to Days</td>
        <td>Seconds</td>
    </tr>
    <tr>
        <td>Compare catalyst performance</td>
        <td>Manual spreadsheet review</td>
        <td>Instant SQL query</td>
    </tr>
    <tr>
        <td>Identify optimal conditions</td>
        <td>Expensive trial-and-error</td>
        <td>ML-driven optimization</td>
    </tr>
    <tr>
        <td>Detect degradation</td>
        <td>After failure occurs</td>
        <td>2-3 weeks early warning</td>
    </tr>
    <tr>
        <td>Procurement planning</td>
        <td>Reactive purchasing</td>
        <td>Forecast-based strategy</td>
    </tr>
</table>

<hr>

<h2 id="architecture"> Project Architecture</h2>

<pre>
┌─────────────────────────────────────────────────────────────────────────┐
│                    EXPERIMENTAL DATA SOURCES                           │
├────────────┬─────────────┬───────────────┬───────────────┬────────────┤
│  Excel     │    CSV      │  Sensor Logs  │  Historical   │ Electrochem│
│  Files     │   Files     │               │   Records     │  Systems   │
└─────┬──────┴──────┬──────┴───────┬───────┴───────┬───────┴────────┬───┘
      │             │              │               │                │
      └─────────────┴──────────────┴───────────────┴────────────────┘
                                      │
                                      ▼
                      ┌─────────────────────────────────┐
                      │   PHASE 1: ETL DATA PIPELINE  │
                      │  Extract → Transform → Load     │
                      │  (Python + SQLAlchemy)          │
                      └───────────────┬─────────────────┘
                                      │
                                      ▼
                      ┌─────────────────────────────────┐
                      │   PHASE 2: MySQL DATABASE     │
                      │  Structured Experimental DB     │
                      │  • experiments                  │
                      │  • catalyst_information         │
                      │  • membrane_properties          │
                      │  • operating_conditions         │
                      │  • electrochemical_results      │
                      │  • product_analysis             │
                      └───────────────┬─────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────────┐
          │                           │                               │
          ▼                           ▼                               ▼
┌─────────────────┐     ┌─────────────────────────┐   ┌─────────────────────────┐
│   PHASE 3     │     │       PHASE 4              │   │   PHASE 5             │
│  Exploratory    │     │  Statistical Analysis    │   │  Data Preprocessing     │
│  Data Analysis  │     │  • ANOVA                 │   │  • Encoding             │
│  & Feature      │     │  • Correlation           │   │  • Scaling              │
│  Engineering    │     │  • Hypothesis Testing    │   │  • Imputation           │
└─────────────────┘     └─────────────────────────┘   └─────────────────────────┘
          │                           │                               │
          └───────────────────────────┼───────────────────────────────┘
                                      │
                                      ▼
                      ┌─────────────────────────────────┐
                      │   PHASE 6: MACHINE LEARNING   │
                      │  Performance Prediction Models  │
                      │  • Gradient Boosting (R²=0.91) │
                      │  • Random Forest               │
                      │  • XGBoost                     │
                      │  • MLP Neural Network          │
                      └───────────────┬─────────────────┘
                                      │
                                      ▼
                      ┌─────────────────────────────────┐
                      │   PHASE 7: PROCESS OPTIMIZE   │
                      │  • Bayesian Optimization       │
                      │  • Catalyst Selection          │
                      │  • Operating Condition Tuning  │
                      │  • Design-Space Exploration    │
                      └───────────────┬─────────────────┘
                                      │
                                      ▼
                      ┌─────────────────────────────────┐
                      │   PHASE 8: PREDICTIVE MAINT   │
                      │  • Failure Risk Classification │
                      │  • RUL Estimation              │
                      │  • Degradation Tracking        │
                      │  • SHAP Interpretation         │
                      └───────────────┬─────────────────┘
                                      │
                                      ▼
                      ┌─────────────────────────────────┐
                      │   PHASE 9: PROCUREMENT        │
                      │  • Web Scraping                 │
                      │  • ARIMA Price Forecasting     │
                      │  • Market Trend Analysis       │
                      └───────────────┬─────────────────┘
                                      │
                                      ▼
                      ┌─────────────────────────────────┐
                      │   PHASE 10: STREAMLIT DASH    │
                      │  Unified Decision Platform      │
                      │  Real-time Monitoring           │
                      │  Interactive Visualizations     │
                      └─────────────────────────────────┘
</pre>

<hr>


<h3>Phase 1: Data Engineering & ETL Pipeline</h3>
<p><strong>The Problem:</strong> Fragmented experimental data across 23+ files with inconsistent formats, naming conventions, and missing values.</p>
<p><strong>The Solution:</strong> Automated ETL pipeline with Python and Pandas for data extraction, cleaning, transformation, and loading.</p>
<p><strong>Key Actions:</strong></p>
<ul>
    <li>Standardized 47+ column names</li>
    <li>Removed 127 duplicate experiments</li>
    <li>Reduced missing values from 15% to &lt;1%</li>
    <li>Converted 12 unit systems to 3 standard units</li>
    <li>Clean and uniform script with minimized spacing.</li>
</ul>
<p><strong>Result:</strong> Clean, standardized dataset ready for database loading.</p>
<p><strong>Note:</strong> The complete Python implementation, detailed explanations, and preprocessing workflow are available in the <strong>README – 2.Data Cleaning,ETL,  Preprosseing, EDA & Statistical Analysis</strong> section of this repository.</p>

<p align="center">
    <img src="assest/3.png" width="800" alt="EDA Analysis">
</p>
 <hr>

<h3>Phase 2: MySQL Database Development</h3>

<p align="center">
    <img src="assest/s1.png" width="900" alt="Average Yield Results">
</p>


<p><strong>The Problem:</strong> No centralized data storage — data existed in isolated files.</p>
<p><strong>The Solution:</strong> Structured relational database with SQLAlchemy ORM for Python integration.</p>
<p><strong>Database Schema:</strong></p>
<pre>
Electrolyzer_Database
│
├── experiments
├── catalyst_information
├── membrane_properties
├── operating_conditions
├── electrochemical_results
└── product_analysis
</pre>

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


<p><strong>Result:</strong> Centralized, queryable database with SQL-based analytics.</p>
<p><strong>Note:</strong> The complete Python implementation, detailed explanations, and preprocessing workflow are available in the<strong>README – 1.Database, SQLAlechmy, MySQL,SQLLITE</strong> section of this repository.</p>
 <hr>


<h3>Phase 3: Exploratory Data Analysis & Feature Engineering</h3>

<p align="center">
    <img src="assest/2.png" width="900" alt="EDA Analysis">
</p>

<p><strong>The Problem:</strong> Hidden relationships between parameters were unknown.</p>
<p><strong>The Solution:</strong> Comprehensive EDA with correlation analysis, distribution analysis, and outlier detection.</p>
<p><strong>Key Findings:</strong></p>
<ul>
    <li>Strong correlation: Voltage × Methanol Yield (r = 0.78)</li>
    <li>Negative correlation: Temperature × Ethanol Yield (r = -0.65)</li>
    <li>Non-linear relationship: Current Density × Selectivity</li>
</ul>

<p align="center">
    <img src="assest/9.png" width="800" alt="EDA Analysis">
</p>

<p><strong>Key Finding:</strong> Pt-Co alloy catalysts showed <strong>34% higher methanol yield</strong> than pure Pt catalysts.</p>

<h3>Yield Efficiency by Catalyst</h3>

<p align="center">
    <img src="assest/v2.png" width="800" alt="Yield Efficiency Results">
</p>

<p><strong>Key Finding:</strong> Pt-Co achieved <strong>25.4 µmol/mL/hr</strong> — the highest efficiency among tested catalysts.</p>



<p><strong>Top 5 Performance Drivers:</strong></p>
<p><strong>Key Finding:</strong> MX@NG achieved the highest methanol yield (~16 &micro;mol/mL), followed by Pt&ndash;Ni/TiO<sub>2</sub>/g-C<sub>3</sub>N<sub>4</sub>, Pt&ndash;Co/TiO<sub>2</sub>, and Pt&ndash;Co/TiO<sub>2</sub>/g-C<sub>3</sub>N<sub>4</sub>.</p>

<p align="center">
    <img src="assest/v1.png" width="700" alt="Bayesian Optimization">
</p>

<p><strong>Optimization Progress:</strong> Achieved optimal performance after 45 iterations, identifying Pt-Co at 250 mA/cm², 3.2V, 60°C as the optimal condition.</p>


<p><strong>Feature Engineering:</strong></p>
<ul>
    <li>Energy input = Voltage × Current Density × Time</li>
    <li>Scale factor = Electrode Area / 25</li>
    <li>Catalyst loading efficiency = Yield / Metal Loading</li>
    <li>Degradation rate = (Voltage_start - Voltage_end) / Time</li>
</ul>

<p align="center">
    <img src="assest/7.png" width="800" alt="Statistical Target (Methanol)">
</p>


<p><strong>Note:</strong> The complete Python implementation, detailed explanations, and preprocessing workflow are available in the<strong>README – 2.Data Cleaning,ETL,  Preprosseing, EDA & Statistical Analysis</strong> section of this repository.</p>
 <hr>


<h3>Phase 4: Statistical Analysis</h3>

<p><strong>Objective:</strong> Evaluate data characteristics and identify statistically significant patterns affecting catalyst performance.</p>

<p><strong>Key Activities:</strong></p>
<ul>
    <li>Descriptive statistical analysis</li>
    <li>Distribution, skewness, and kurtosis analysis</li>
    <li>Correlation and comparative statistical analysis</li>
    <li>Evlauting the ANOVA, TTEST, Linear Regressor</li>
    
</ul>

<p align="center">
    <img src="assest/ss2.png" width="800" alt="Statistical Analysis">
</p>



  <strong>OLS Regression Insight – Methanol Yield vs. Cathode Loading</strong>
  <br><br>
  The OLS analysis (815 samples) shows a statistically significant relationship between cathode loading and methanol yield (p &lt; 0.001).
  <br><br>
  <strong>Key Findings:</strong>
  <ul>
    <li>Cathode loading has a negative effect, with each 1 mg/cm² increase reducing methanol yield by approximately 0.12 µmol/ml.</li>
    <li>The model explains ~9.6% of yield variation (R² = 0.096), indicating that other factors such as voltage, catalyst composition, and operating conditions have stronger impacts.</li>
    <li>Residual analysis confirms no major autocorrelation or multicollinearity issues.</li>
  </ul>

  <strong>Conclusion:</strong> Cathode loading is a significant but limited predictor; optimal catalyst performance requires considering multiple interacting parameters.</div>

<p align="center">
    <img src="assest/ss3.png" width="800" alt="Statistical Analysis">
</p>

<p><strong>Statistical Summary:</strong> Methanol yield averaged <strong>3.94 mL</strong> (SD = <strong>4.81 mL</strong>, CV = <strong>122.13%</strong>), indicating high variability across experimental conditions.</p>

<p align="center">
    <img src="assest/ss1.png" width="800" alt="Statistical Target (Methanol)">
</p>

<p><strong>Note:</strong> Complete statistical analysis, visualizations, and detailed explanations are available in the <strong>README – 2. Data Cleaning, ETL, Preprocessing, Feature Engineering, EDA & Statistical Analysis</strong> section.</p>

<hr>

<h3>Phase 5: Data Preprocessing Pipeline</h3>
<p><strong>The Problem:</strong> Raw data not suitable for ML algorithms.</p>
<p><strong>The Solution:</strong> Automated Scikit-learn pipeline with ColumnTransformer.</p>
<p><strong>Pipeline Components:</strong></p>
<ul>
    <li>Missing value imputation (mean for numerical, mode for categorical)</li>
    <li>One-hot & Label encoding for categorical variables</li>
    <li>StandardScaler for numerical features</li>
    <li>SMOTE for handling class imbalance</li>
</ul>

<p align="center">
    <img src="assest/8.png" width="800" alt="Statistical Target (Methanol)">
</p>

<h3>Column Transformation Using ColumnTransformer</h3>

<p>
A unified preprocessing workflow was developed using <strong>Scikit-learn ColumnTransformer</strong> to handle
numerical and categorical features separately within a single pipeline.
</p>

<pre>
preprocessor = ColumnTransformer( transformers=[("num", numeric_pipeline, numerical_features),
        ("cat", categorical_pipeline, categorical_features)])
</pre>

<p>
<strong>Benefits:</strong>
</p>

<ul>
<li>Automated feature transformation</li>
<li>Consistent training and prediction workflow</li>
<li>Reduced preprocessing errors</li>
<li>Deployment-ready ML pipeline</li>
</ul>

<h3>Handling Class Imbalance Using SMOTE</h3>
<p>
Electrolyzer failure datasets usually contain fewer failure events compared with normal operation, creating an
imbalanced classification problem.
</p>

<ul>
<li><strong>Normal Condition:</strong> Majority class</li>
<li><strong>Warning Condition:</strong> Minority class</li>
<li><strong>Critical Failure:</strong> Minority class</li>
</ul>

<p>
To improve model learning during development, <strong>SMOTE (Synthetic Minority Oversampling Technique)</strong> was
applied to generate synthetic samples for minority classes by interpolating between existing observations.
</p>

<pre>
smote = SMOTE( random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
</pre>

<p>
<strong>Important:</strong> SMOTE was applied only to the training dataset to prevent data leakage.
The final deployment pipeline uses the trained model and preprocessing workflow without synthetic data generation.
</p>

<p><strong>Note:</strong> The complete Python implementation, detailed explanations, and preprocessing workflow are available in the<strong>README – 3.ML models  to optimize catalyst performance and operational parameters and also 5.ML–Based Electrolyzer Predictive Maintenance</strong> section of this repository.</p>


 <hr>

<h3>Phase 6: Machine Learning Models for Catalyst Design & Production Predict</h3>

<p align="center">
    <img src="assest/m1.png" width="900" alt="Statistical Target (Methanol)">
</p>


<p>
<strong>Reference:</strong><br>
ScienceDirect Article:
<a href="https://www.sciencedirect.com/science/article/abs/pii/S0013468626005700" target="_blank">
https://www.sciencedirect.com/science/article/abs/pii/S0013468626005700
</a>
</p>

<p><strong>The Problem:</strong> Need to predict performance without running experiments.</p>
<p><strong>The Solution:</strong> 4 ML models with hyperparameter optimization.</p>
<p><strong>Results:</strong></p>

<p><strong>ML-Based Catalyst Ranking:</strong> A machine learning framework was developed to reduce experimental effort by predicting and ranking multi-metal electrocatalyst performance. Among 25 candidates, Ti(TiCN) achieved the highest normalized score (100), followed by Ru-Pd (29.46), Pt-Ni-Pd (21.66), and Pt-Co (13.85). Based on performance ranking and Pt-Co synergistic effects for CH₄ activation, Pt-Co was selected for experimental validation.</p>


<table border="1" cellpadding="5">
    <tr>
        <th>Model</th>
        <th>Methanol R²</th>
        <th>Methanol RMSE</th>
        <th>Ethanol R²</th>
        <th>Ethanol RMSE</th>
    </tr>
    <tr>
        <td><strong>Gradient Boosting</strong></td>
        <td><strong>0.9139</strong></td>
        <td><strong>0.9643</strong></td>
        <td><strong>0.9066</strong></td>
        <td><strong>0.7891</strong></td>
    </tr>
    <tr>
        <td>ANN</td>
        <td>0.8916</td>
        <td>1.0819</td>
        <td>0.8943</td>
        <td>0.8394</td>
    </tr>
    <tr>
        <td>SVR</td>
        <td>0.8802</td>
        <td>1.1375</td>
        <td>0.8828</td>
        <td>0.8839</td>
    </tr>
    <tr>
        <td>Random Forest</td>
        <td>0.8798</td>
        <td>1.1395</td>
        <td>0.8517</td>
        <td>0.9943</td>
    </tr>
</table>

<p align="center">
    <img src="assest/10.png" width= "600" alt="Statistical Target (Methanol)">
</p>

<h3> Feature Importance Analysis</h3>

<p align="center">
    <img src="assest/11.png" width="800" alt="Feature Importance">
</p>



<h3> Effect of CH₄ Flow Rate on Catalyst Performance</h3>

<p><strong>Key Finding:</strong> Methane flow rate significantly influences catalyst activity and methanol production. The analysis shows that an optimal CH₄ flow rate of approximately <strong>40 sccm</strong> provides the highest average methanol yield, while lower or higher flow rates result in reduced performance.</p>

<p><strong>Interpretation:</strong> An optimized methane supply improves reactant availability and mass transfer, enhancing catalytic conversion efficiency. Excessive flow rates may reduce residence time and limit conversion, whereas insufficient flow can restrict reaction kinetics.</p>

<p align="center">
    <img src="assest/4.png" width="500" alt="Statistical Target (Methanol)">
</p>

<p align="center">
    <img src="assest/5.png" width="500" alt="Statistical Target (Methanol)">
</p>

<p align="center">
    <img src="assest/6.png" width="500" alt="Statistical Target (Methanol)">
</p>


<p><strong>Key Finding:</strong> Methanol and ethanol yields reached their maximum at <strong>6 hours</strong> of reaction time. Longer reaction periods showed diminishing returns, indicating that ~6 hours is the optimal operating duration for efficient alcohol production.</p>

<p align="center">
    <img src="assest/v3.png" width="900" alt="Catalyst Performance Comparison">
</p>

<table border="1" cellpadding="5">
    <tr>
        <th>Parameter</th>
        <th>Optimal Value</th>
        <th>Improvement</th>
    </tr>
    <tr>
        <td>Catalyst Type</td>
        <td>Pt-Co (5% loading)</td>
        <td>34% better than Pt</td>
    </tr>
    <tr>
        <td>Current Density</td>
        <td>40 mA/cm²</td>
        <td>22% better at peak</td>
    </tr>
    <tr>
        <td>Voltage</td>
        <td>1.5 V</td>
        <td>Optimal window</td>
    </tr>
    <tr>
        <td>Temperature</td>
        <td>60°C</td>
        <td>Nonlinear optimum</td>
    </tr>
    <tr>
        <td>Reaction Time</td>
        <td>6 hours</td>
        <td>Before degradation</td>
    </tr>
</table>

<p><strong>Note:</strong> The complete Python implementation, detailed explanations, and preprocessing workflow are available in the<strong>README – 3.ML models  to optimize catalyst performance and operational parameters </strong> section of this repository.</p>




<p><strong>Note:</strong> The complete Python implementation, detailed explanations, and preprocessing workflow are available in the<strong>README – 3.ML models  to optimize catalyst performance and operational parameters </strong> section of this repository.</p>
 <hr>


<h2> Phase 7: Machine Learning Models for CH₄ Electrolyzer Process Optimization & Scale-Up </h2>


<p align="center">
    <img src="assest/1.png" width="900" alt="CH4 Electrolyzer">
</p>

<h3>Why Ensemble Learning?</h3>

<p>
<strong>Challenge:</strong> Scaling CH₄ electrolyzers from <strong>5 cm²</strong> laboratory cells to
<strong>25 cm²</strong> pilot-scale systems introduces complex nonlinear interactions between catalyst properties and operating conditions, making accurate yield prediction difficult.
</p>

<p>
<strong>Solution:</strong> Ensemble learning combines multiple machine learning models to improve
<strong>prediction accuracy, robustness, and generalization</strong> compared with a single algorithm.
In this study, <strong>Decision Tree, Random Forest, Gradient Boosting, and XGBoost</strong> were evaluated to predict
<strong>methanol and ethanol yields</strong> and identify the optimal operating conditions for electrolyzer scale-up.
</p>

<table border="1" cellpadding="6" cellspacing="0">
<tr>
<th>Technique</th>
<th>Purpose</th>
</tr>

<tr>
<td><strong>Decision Tree</strong></td>
<td>Captures simple decision rules and provides an interpretable baseline model.</td>
</tr>

<tr>
<td><strong>Random Forest</strong></td>
<td>Reduces overfitting and improves prediction stability through bagging.</td>
</tr>

<tr>
<td><strong>Gradient Boosting</strong></td>
<td>Sequentially improves weak learners to enhance predictive performance.</td>
</tr>

<tr>
<td><strong>XGBoost</strong></td>
<td>Optimizes accuracy, regularization, and computational efficiency for complex datasets.</td>
</tr>

</table>

<p>
Overall, ensemble learning provides a reliable <strong>data-driven framework</strong> for predicting alcohol yields,
identifying key process variables, and supporting the successful scale-up of CH₄ electrolyzers from
<strong>5 cm²</strong> to <strong>25 cm²</strong>.
</p>




<h3>Best Model Parameters</h3>
<h3>Hyperparameter Optimization</h3>

<p>
Tree-based ensemble models were optimized using <strong>GridSearchCV with cross-validation</strong> to improve prediction accuracy and reduce overfitting. The optimization focused on tree depth, number of estimators, learning rate, and sampling parameters.
</p>

<table border="1" cellpadding="8" cellspacing="0">

<thead>
<tr>
<th>Model</th>
<th>Optimized Hyperparameters</th>
</tr>
</thead>

<tbody>

<tr>
<td><strong>Decision Tree</strong></td>
<td>max_depth, min_samples_split, min_samples_leaf</td>
</tr>

<tr>
<td><strong>Random Forest</strong></td>
<td>n_estimators, max_depth, min_samples_split</td>
</tr>

<tr>
<td><strong>Gradient Boosting</strong></td>
<td>n_estimators, learning_rate, max_depth, subsample</td>
</tr>

</tbody>

</table>

<h3>Best Model Parameters</h3>

<table border="1" cellpadding="8" cellspacing="0">

<tr>
<th>Model</th>
<th>Final Parameters</th>
</tr>

<tr>
<td><strong>Decision Tree</strong></td>
<td>Best parameters selected automatically using GridSearchCV.</td>
</tr>

<tr>
<td><strong>Random Forest</strong></td>
<td>300 estimators, unlimited tree depth, minimum split = 2.</td>
</tr>

<tr>
<td><strong>Gradient Boosting</strong></td>
<td>500 estimators, learning rate = 0.05, maximum depth = 6.</td>
</tr>

</table>

<p>
Hyperparameter tuning significantly improved model generalization, with the optimized ensemble models achieving higher prediction accuracy and reduced overfitting for CH₄ electrolyzer performance prediction.
</p>

<p align="center">
<img src="assest/DT.png" width="900" alt="Decision Tree Hyperparameter Optimization">
</p>

<p align="center">
<img src="assest/RF.png" width="900" alt="Random Forest Hyperparameter Optimization">
</p>

<p><b>Final Model Selection:</b> ✅ XGBoost - Highest test R² (0.8345), lowest test RMSE (1.4358), lowest test MAE (0.9322), best generalization capability.</p>

<h3>Model Comparison & Performance</h3>
<pre>
models = {
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
    'XGBoost': XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)}
</pre>


<p>
The following plots present the performance evaluation and prediction behavior of the developed ensemble models.
These visualizations demonstrate model accuracy, generalization capability, and prediction reliability for CH₄ electrolyzer yield optimization.
</p>

<p align="center">
<img src="assest/5.1.png" width="900" alt="Electrolyzer Yield Prediction Results">
</p>

<h3>Random Forest Regressor - Model Diagnostics</h3>

<p>
Residual analysis was performed to validate the Random Forest model for predicting methanol yield from CH₄ electrochemical conversion. The diagnostic plots confirm model reliability, prediction consistency, and error behavior.
</p>

<ul>
  <li><strong>Residual Distribution:</strong> Errors are randomly distributed around zero, indicating low prediction bias.</li>
  <li><strong>Standardized Residuals:</strong> Most residuals remain within ±2σ, confirming stable variance.</li>
  <li><strong>Predicted vs Actual:</strong> Predictions closely follow the ideal y=x line, demonstrating good agreement with experimental values.</li>
  <li><strong>Q-Q Plot:</strong> Residuals approximately follow normal distribution with minor deviations due to experimental variability.</li>
  <li><strong>Outlier Detection:</strong> A small number of outliers were identified, likely caused by extreme operating conditions or measurement uncertainty.</li>
</ul>

<p>
<strong>Overall:</strong> The Random Forest model achieved strong predictive performance 
(<strong>Test R² = 0.819, RMSE = 1.501 µmol/mL</strong>) and effectively captured nonlinear relationships between catalyst properties, operating conditions, and methanol yield.
</p>

<p align="center">
<img src="assest/16.png" width="900" alt="Electrolyzer Yield Prediction Results">
</p>


<h3>3D Surface Plot Analysis: Methanol Yield Optimization</h3>

<p>
The 3D surface plot illustrates the interaction between <strong>current density</strong>,
<strong>reaction time</strong>, and <strong>methanol yield</strong> in CH₄ electrochemical conversion.
</p>

<ul>
  <li><strong>Optimal Conditions:</strong> Maximum yield occurs at approximately
  <strong>40–60 mA/cm²</strong> and <strong>4–6 hours</strong> reaction time.</li>

  <li><strong>Performance Limitation:</strong> Low current reduces reaction activity, while excessive current
  and extended operation can increase degradation and side reactions.</li>

  <li><strong>Scale-Up Application:</strong> The optimized operating window supports transition from
  <strong>5 cm² laboratory cells</strong> to <strong>25 cm² pilot-scale electrolyzers</strong>.</li>
</ul>

<p>
<strong>Conclusion:</strong> The ML-based surface analysis identifies optimal operating regions and captures
nonlinear parameter interactions for data-driven methanol yield optimization.
</p>

<p align="center">
<img src="assest/17.png" width="900" alt="3D Surface Plot Analysis">
</p>

<p><strong>Note:</strong> The complete Python implementation, detailed explanations, and preprocessing workflow are available in the<strong>README – 4.ML for CH4 Electolyzer Optimization and Prediction </strong> section of this repository.</p>

 <hr>


<h3> Phase 8: Machine Learning Classification for Electrolyzer Predictive Maintenance and Failure Risk Detection </h3>

<p align="center">
<img src="assest/21.png" width="900" >
</p>

<p>
<strong>The Problem:</strong> Unexpected electrolyzer failures can cause performance degradation,
costly downtime, and reliability challenges during scale-up from <strong>5 cm² laboratory cells</strong>
to <strong>25 cm² pilot-scale systems</strong>.
</p>

<p>
<strong>The Solution:</strong> An end-to-end machine learning framework was developed using
<strong>classification models with SMOTE-based imbalance handling</strong> to improve failure detection
and maintenance prediction.
</p>

<ul>
<li>
<strong>Failure Risk Prediction:</strong> Multi-class classification of system health into
<strong>Normal, Warning, and Critical</strong> conditions for early fault detection.
</li>

<li>
<strong>Maintenance Prediction:</strong> Binary classification to predict maintenance requirements
(<strong>Yes/No</strong>) and support proactive operation planning.
</li>
</ul>

<p>
The framework integrates <strong>ETL preprocessing, feature engineering, ensemble machine learning,
cross-validation, and deployment-ready pipelines</strong> for reliable electrolyzer monitoring.
</p>

<p>
<strong>Scale-Up Impact:</strong> The model identifies degradation risks associated with
<strong>non-uniform current distribution, thermal gradients, and mass transport limitations</strong>,
supporting reliable transition from laboratory to pilot-scale electrolyzer operation.
</p>


<h3>Decision Tree: Imbalance Handling Analysis</h3>

<p>
The Decision Tree model was evaluated with different imbalance-handling techniques to improve
<strong>maintenance/failure detection</strong>. Since failure cases are rare, recall of the minority class
is more important than accuracy alone.
</p>

<ul>
<li>
<strong>Without SMOTE:</strong> High accuracy (89%) but failed to detect any maintenance cases
(Recall = 0%), showing strong bias toward normal operation.
</li>

<li>
<strong>SMOTE / SMOTEENN:</strong> Improved failure detection by increasing minority-class recall to
<strong>75%</strong>, but produced more false positives.
</li>

<li>
<strong>SMOTETomek:</strong> Provided the best balance, achieving <strong>79% accuracy</strong>,
<strong>75% recall</strong>, and the highest <strong>F1-score (0.30)</strong>.
</li>

<li>
<strong>Threshold tuning:</strong> Increased model sensitivity to critical events, which is essential
for predictive maintenance applications.
</li>
</ul>

<p>
<strong>Conclusion:</strong> SMOTETomek with threshold tuning provides the most suitable approach for
early electrolyzer failure detection by improving minority-class identification while maintaining
acceptable prediction stability.
</p>

<p align="center">
<img src="assest/18.png" width="900">
</p>



<p><b>Ensemble Model Comparison with Threshold Tuning</b></p>

<p>
Random Forest, Gradient Boosting, and Decision Tree models were evaluated using
<b>SMOTETomek, preprocessing pipeline, and threshold tuning (0.25)</b> to improve
rare failure detection.
</p>

<ul>
<li>
<b>Gradient Boosting:</b> Achieved the best balance with
<b>86.4% accuracy</b>, <b>F1-score = 0.31</b>, and <b>50% recall</b> for failure cases.
</li>

<li>
<b>Threshold tuning:</b> Increased sensitivity toward minority failure events compared
with default classification threshold.
</li>

<li>
<b>Limitation:</b> Very limited failure samples caused low precision and false alarms.
</li>
</ul>

<p>
<b>Conclusion:</b> Gradient Boosting is the most suitable baseline model for
electrolyzer predictive maintenance due to better balance between failure detection
and prediction reliability.
</p>

<p align="center">
<img src="assest/19.png" width="900">
</p>


<p><b>Multi-Class ROC Analysis Insight</b></p>

<p>
ROC analysis shows strong performance for identifying healthy electrolyzer operation
and lower performance for rare failure categories.
</p>

<ul>
<li><b>Normal Class:</b> Excellent detection with <b>AUC = 0.99</b>.</li>
<li><b>Warning Class:</b> Moderate detection with <b>AUC = 0.64</b>.</li>
<li><b>Critical Class:</b> Poor detection with <b>AUC = 0.45</b> due to limited failure data and overlapping patterns.</li>
</ul>

<p>
<b>Key Insight:</b> Additional degradation features, time-series indicators, and more
failure samples are required to improve early warning and critical failure prediction.
</p>

<p align="center">
<img src="assest/20.webp" width="500">
</p>



<p><b>Bayesian Optimization for Degradation Minimization</b></p>

<p>
A Gradient Boosting degradation model was optimized using Bayesian Optimization
to identify operating conditions that reduce electrolyzer degradation.
</p>

<ul>
<li><b>Optimal conditions:</b> 1.0 V voltage, 50 mA/cm² current density,
0.5 hr reaction time, 20 bar pressure, and no H₂O₂.</li>

<li><b>Predicted degradation:</b> 43.93% under optimized conditions.</li>

<li><b>Main drivers:</b> Voltage, current density, reaction time, and electrolyte composition
strongly affect degradation behavior.</li>
</ul>

<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse; width:100%;">
<tr>
<th>Parameter</th>
<th>Optimal Value</th>
<th>Effect</th>
</tr>

<tr><td>Voltage</td><td>1.0 V</td><td>Reduces electrochemical stress.</td></tr>
<tr><td>Pressure</td><td>20 bar</td><td>Improves operating stability.</td></tr>
<tr><td>Current Density</td><td>50 mA/cm²</td><td>Minimizes thermal and catalyst stress.</td></tr>
<tr><td>Reaction Time</td><td>0.5 hr</td><td>Reduces cumulative degradation.</td></tr>
<tr><td>Na₂CO₃ / KOH</td><td>1.0 M</td><td>Enhances electrolyte stability.</td></tr>
<tr><td>H₂O₂</td><td>0 %</td><td>Avoids oxidative degradation.</td></tr>

</table>

<p>
<b>Conclusion:</b> The optimized parameters reduce degradation by minimizing
operational stress. Experimental validation is recommended before scaling from
5 cm² to 25 cm² electrolyzer systems.
</p>

<p><strong>Note:</strong> The complete Python implementation, detailed explanations, and preprocessing workflow are available in the<strong>README – 5.ML–Based Electrolyzer Predictive Maintenance </strong> section of this repository.</p>
 <hr>


<h2> Phase 9: Automated Web Scraping Pipeline for Electrolyzer Material Price Monitoring and Database Management </h2>

<p align="center">
<a href="https://youtu.be/i90PSh_6ALE" target="_blank">
<img src="https://img.youtube.com/vi/i90PSh_6ALE/maxresdefault.jpg" width="900">
</a>
</p>


<p align="center">
  <a href="https://youtu.be/i90PSh_6ALE" target="_blank">
    <img src="assets/demo_thumbnail.png" width="900" alt="Project Demo">
  </a>
</p>

<p><strong>The Challenge:</strong> The cost and availability of key electrolyzer materials—including lithium carbonate, copper, caustic soda, and soda ash—change continuously due to market fluctuations, creating uncertainty in procurement planning and project budgeting.</p>

<p><strong>The Solution:</strong> An end-to-end procurement intelligence pipeline was developed by integrating automated web scraping, SQLite database management, time-series forecasting, analytics, and email notification into a single Streamlit application.</p>

<p><strong>Key Features:</strong></p>
<ul>
    <li>Automated web scraping (Beautifulsoap) of commodity and chemical prices from online market sources.</li>
    <li>Data cleaning, validation, and historical price archiving in a SQLite database.</li>
    <li>Time-series forecasting using <strong>Prophet</strong> to predict future price trends and market behavior.</li>
    <li>Interactive dashboards for historical trends, forecasting, and procurement analytics.</li>
    <li>Automated email alerts when commodity prices exceed user-defined thresholds.</li>
    <li>Database management tools for querying, exporting, and maintaining historical procurement records.</li>
    <li>Decision-support insights to optimize purchasing schedules and reduce procurement risk.</li>
</ul>

<p><strong>Technologies Used:</strong> Python, Streamlit, BeautifulSoup, Requests, SQLite, Prophet, Plotly, Pandas, SQL, Email Automation.</p>

<p><strong>Project Outcome:</strong> The platform transforms raw online market information into actionable procurement intelligence, enabling proactive purchasing decisions, reducing material cost uncertainty, and supporting electrolyzer scale-up planning.</p>

<p><strong>Note:</strong> The complete implementation, including the web scraping pipeline, SQLite database design, Prophet forecasting model, dashboard development, email alert system, SQL queries, and source code, is available in the <strong>6.WebScarpping for Chemical Price Monitoring, Forecasting</strong> section of this repository.</p>



<hr>


<h2 id="conclusion">Conclusion: From 5 cm² to 25 cm² — A Data-Driven Scale-Up Framework</h2>

<p>This project demonstrates that the future of electrochemical engineering lies at the intersection of experimental science and data intelligence. By building a digital layer on top of our experimental workflows, we can:</p>
<ul>
    <li> <strong>See patterns</strong> that were previously invisible</li>
    <li> <strong>Predict outcomes</strong> before they happen</li>
    <li> <strong>Make decisions</strong> with confidence</li>
    <li> <strong>Accelerate innovation</strong> in clean energy technology</li>
</ul>

<h3>Scale-Up Summary</h3>

<p><strong>The Challenge:</strong> Scaling CH₄ electrolyzers from 5 cm² laboratory cells to 25 cm² pilot-scale systems introduces complex challenges including non-uniform current distribution, mass transport limitations, thermal gradients, and increased degradation risk. Operating conditions optimized at 5 cm² cannot be directly transferred to 25 cm² without adjustment.</p>

<p><strong>The Solution:</strong> This 10-phase ML-driven framework provides a comprehensive pathway for successful scale-up:</p>

<table border="1" cellpadding="5">
    <tr>
        <th>Phase</th>
        <th>Focus</th>
        <th>Scale-Up Contribution</th>
    </tr>
    <tr>
        <td>1-2</td>
        <td>Data Engineering & Database</td>
        <td>Centralized, clean data foundation for scale-up analysis</td>
    </tr>
    <tr>
        <td>3-5</td>
        <td>EDA, Statistics & Preprocessing</td>
        <td>Identifies scale-dependent patterns and prepares data for ML</td>
    </tr>
    <tr>
        <td>6</td>
        <td>ML Models for Catalyst Design</td>
        <td>Predicts performance at scale without costly experiments</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Process Optimization</td>
        <td>Identifies optimal operating conditions for 25 cm² operation</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Predictive Maintenance</td>
        <td>Early warning system for scale-up failures</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Procurement Intelligence</td>
        <td>Cost-effective material sourcing for scale-up</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Streamlit Dashboard</td>
        <td>Real-time monitoring and decision support at scale</td>
    </tr>
</table>

<h3>Key Scale-Up Insights</h3>
<ul>
    <li><strong>Current Density:</strong> Optimal increases from 40 mA/cm² (5 cm²) to 55 mA/cm² (25 cm²)</li>
    <li><strong>Voltage:</strong> Optimal increases from 1.5V to 1.8V to overcome increased resistance</li>
    <li><strong>Temperature:</strong> Slight decrease from 60°C to 55°C to minimize degradation</li>
    <li><strong>Reaction Time:</strong> Decreases from 6 to 5 hours due to faster transport limitations</li>
    <li><strong>Pressure:</strong> Significant increase from 1 atm to 2.5 atm for improved solubility</li>
</ul>

<h3>Predicted 25 cm² Performance</h3>
<table border="1" cellpadding="5">
    <tr>
        <th>Metric</th>
        <th>5 cm² Baseline</th>
        <th>25 cm² Optimized</th>
        <th>Improvement</th>
    </tr>
    <tr>
        <td>Methanol Yield</td>
        <td>3.94 µmol/mL</td>
        <td><strong>4.67 µmol/mL</strong></td>
        <td>⬆ +18.5%</td>
    </tr>
    <tr>
        <td>Ethanol Yield</td>
        <td>2.16 µmol/mL</td>
        <td><strong>2.54 µmol/mL</strong></td>
        <td>⬆ +17.6%</td>
    </tr>
    <tr>
        <td>Methanol Selectivity</td>
        <td>64.6%</td>
        <td><strong>68.2%</strong></td>
        <td>⬆ +3.6%</td>
    </tr>
    <tr>
        <td>Energy Efficiency</td>
        <td>42.3%</td>
        <td><strong>45.1%</strong></td>
        <td>⬆ +2.8%</td>
    </tr>
</table>

<h3>Engineering Recommendations for Successful Scale-Up</h3>
<ol>
    <li><strong>Hardware:</strong> Use uniform compression, 250 µm PTFE gasket, and titanium-based PTL</li>
    <li><strong>Flow Field:</strong> Adopt serpentine design for uniform CH₄ distribution</li>
    <li><strong>Thermal Management:</strong> Implement active cooling to maintain uniform temperature</li>
    <li><strong>Operating Window:</strong> Target 55 mA/cm², 1.8V, 55°C, 5 hr reaction time</li>
    <li><strong>Validation:</strong> Experimentally validate ML predictions at 25 cm² pilot scale</li>
</ol>

<h2>Key Results </h2>

<h3> Data Engineering & Experimental Data Intelligence</h3>
<ul>
    <li>Standardized <strong>47+ experimental parameters</strong> from fragmented Excel, CSV, and laboratory files.</li>
    <li>Removed <strong>127 duplicate experiments</strong> and reduced missing data from <strong>~15% to &lt;1%</strong>.</li>
    <li>Converted <strong>12 unit systems into 3 standardized engineering units</strong>.</li>
    <li>Developed an automated ETL workflow using <strong>Python, Pandas, and SQLAlchemy</strong>.</li>
    <li>Built a centralized <strong>MySQL experimental database</strong> for catalyst, membrane, operating conditions, electrochemical results, and product analysis.</li>
</ul>

<p><strong>Result:</strong> A clean, standardized, and query-ready database enabling data-driven electrochemical analysis.</p>


<h3> Statistical Analysis & Engineering Insights</h3>
<ul>
    <li>Performed correlation analysis, ANOVA, hypothesis testing, and OLS regression to identify key performance drivers.</li>
    <li>Found that increasing cathode loading by <strong>1 mg/cm² reduced methanol yield by ~0.12 µmol/mL</strong>.</li>
    <li>OLS regression explained <strong>9.6% of yield variation (R² = 0.096)</strong>, showing stronger influence from catalyst composition and operating conditions.</li>
    <li>Residual analysis confirmed no major autocorrelation or multicollinearity issues.</li>
</ul>

<p><strong>Result:</strong> Identified critical engineering factors controlling catalyst performance.</p>


<h3> Machine Learning Performance Prediction</h3>
<ul>
    <li>Developed ML models for CH₄ electrochemical conversion performance prediction.</li>
    <li><strong>Methanol Yield:</strong> Gradient Boosting achieved <strong>R² = 0.9139</strong>.</li>
    <li><strong>Ethanol Yield:</strong> Gradient Boosting achieved <strong>R² = 0.9066</strong>.</li>
    <li>Evaluated Random Forest, XGBoost, SVR, ANN, and ensemble models.</li>
    <li>Applied feature importance and SHAP analysis to identify dominant process variables.</li>
</ul>

<p><strong>Result:</strong> Reduced experimental trial-and-error through accurate ML-based prediction.</p>


<h3> Catalyst Selection & Process Optimization</h3>
<ul>
    <li>Identified optimal CH₄ electrolysis conditions:</li>
    <ul>
        <li><strong>Catalyst:</strong> Pt-Co</li>
        <li><strong>Current Density:</strong> 40–60 mA/cm²</li>
        <li><strong>Voltage:</strong> 1.5 V</li>
        <li><strong>Temperature:</strong> 60°C</li>
        <li><strong>Reaction Time:</strong> ~6 hours</li>
    </ul>
    <li>Feature analysis identified catalyst type, voltage, current density, and reaction time as key performance drivers.</li>
</ul>

<p><strong>Result:</strong> Enabled data-driven catalyst ranking and process optimization.</p>


<h3> Electrolyzer Scale-Up Optimization (5 cm² → 25 cm²)</h3>
<ul>
    <li>Developed an ML-guided framework for laboratory-to-pilot scale transition.</li>
    <li>Optimized operating conditions:</li>
    <ul>
        <li>Current density: <strong>40 → 55 mA/cm²</strong></li>
        <li>Voltage: <strong>1.5 → 1.8 V</strong></li>
        <li>Temperature: <strong>60 → 55°C</strong></li>
        <li>Reaction time: <strong>6 → 5 hours</strong></li>
        <li>Pressure: <strong>1 → 2.5 atm</strong></li>
    </ul>
</ul>

<p><strong>Predicted Improvements:</strong></p>
<ul>
    <li>Methanol yield: <strong>+18.5%</strong></li>
    <li>Ethanol yield: <strong>+17.6%</strong></li>
    <li>Methanol selectivity: <strong>+3.6%</strong></li>
    <li>Energy efficiency: <strong>+2.8%</strong></li>
</ul>


<h3> Predictive Maintenance & Failure Risk Detection</h3>
<ul>
    <li>Developed ML classification models for electrolyzer health monitoring.</li>
    <li>Applied <strong>SMOTE, SMOTEENN, SMOTETomek, and threshold tuning</strong> for rare failure detection.</li>
    <li>Gradient Boosting achieved:</li>
    <ul>
        <li>Accuracy: <strong>86.4%</strong></li>
        <li>Recall: <strong>50%</strong></li>
        <li>F1-score: <strong>0.31</strong></li>
    </ul>
    <li>ROC performance:</li>
    <ul>
        <li>Normal operation: <strong>AUC = 0.99</strong></li>
        <li>Warning condition: <strong>AUC = 0.64</strong></li>
        <li>Critical failure: <strong>AUC = 0.45</strong></li>
    </ul>
</ul>

<p><strong>Result:</strong> Developed an early-warning framework for electrolyzer reliability improvement.</p>


<h3> Degradation Optimization Using Bayesian Optimization</h3>
<ul>
    <li>Combined Gradient Boosting degradation modeling with Bayesian Optimization.</li>
    <li>Identified optimal conditions:</li>
    <ul>
        <li>Voltage: <strong>1.0 V</strong></li>
        <li>Current density: <strong>50 mA/cm²</strong></li>
        <li>Pressure: <strong>20 bar</strong></li>
        <li>Reaction time: <strong>0.5 h</strong></li>
        <li>Electrolyte: <strong>1.0 M Na₂CO₃/KOH</strong></li>
        <li>H₂O₂: <strong>0%</strong></li>
    </ul>
</ul>

<p><strong>Result:</strong> Identified operating conditions to minimize degradation and improve long-term stability.</p>


<h3>✅ Procurement Intelligence & Price Forecasting</h3>
<ul>
    <li>Developed automated material monitoring using <strong>BeautifulSoup web scraping</strong>.</li>
    <li>Stored historical prices using <strong>SQLite database</strong>.</li>
    <li>Applied <strong>Prophet time-series forecasting</strong> for price prediction.</li>
    <li>Created Streamlit dashboards with automated email alerts.</li>
    <li>Monitored critical materials including lithium carbonate, copper, caustic soda, and soda ash.</li>
</ul>

<p><strong>Result:</strong> Enabled proactive procurement decisions and reduced supply-chain uncertainty.</p>


