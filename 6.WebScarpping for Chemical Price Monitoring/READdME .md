

<h1> Automated Web Scraping Pipeline for Electrolyzer Material Price Monitoring and Database Management</h1>
<h2>From Raw Market Data to Predictive Supply Chain Decisions</h2>

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

<hr>


<h2 id="overview">1. Overview</h2>

<p>Scaling electrolyzer technologies from laboratory systems to pilot and industrial operation requires not only engineering optimization but also <b>intelligent material supply chain management</b>.</p>

<p>Critical electrolyzer components such as catalysts, metals, and supporting materials are exposed to significant market volatility. Unexpected price changes in materials like <b>lithium carbonate, copper, soda ash, and caustic soda</b> can directly impact manufacturing cost, project planning, and technology scale-up decisions.</p>

<p>This project develops an <b>end-to-end procurement intelligence platform</b> that transforms real-time commodity market information into actionable insights using:</p>

<ul>
    <li>Automated Web Scraping</li>
    <li>Data Engineering Pipeline</li>
    <li>SQLite Database Management</li>
    <li>Time-Series Forecasting</li>
    <li>Price Analytics</li>
    <li>Automated Alert System</li>
    <li>Interactive Streamlit Dashboard</li>
</ul>

<hr>

<h2 id="objective">2. Project Objective</h2>

<p>The objective is to build a digital intelligence system capable of:</p>

<ol>
    <li>Automatically collecting commodity price data from online sources</li>
    <li>Storing historical market information in a structured database</li>
    <li>Forecasting future price trends using machine learning models</li>
    <li>Monitoring critical price thresholds</li>
    <li>Providing automated alerts for procurement decisions</li>
</ol>

<p>The final system acts as a <b>decision-support tool for electrolyzer material procurement and cost-risk management</b>.</p>

<hr>

<h2 id="motivation">3. Engineering Motivation: Why Material Intelligence Matters?</h2>

<p>Electrolyzer scale-up introduces new challenges:</p>

<ul>
    <li>Larger electrode areas increase material requirements</li>
    <li>Catalyst and metal costs become significant contributors to capital expenditure</li>
    <li>Supply chain fluctuations affect manufacturing economics</li>
    <li>Early prediction of price trends enables better procurement strategies</li>
</ul>

<p>Therefore, combining <b>chemical engineering knowledge with data engineering and forecasting</b> creates a smarter approach for electrolyzer deployment.</p>

<hr>

<h2 id="architecture">4. System Architecture</h2>

<pre>
                Commodity Websites
                       |
                       ↓
            Automated Web Scraping
            (Requests + BeautifulSoup)
                       |
                       ↓
             Data Cleaning & Processing
                   (Pandas)
                       |
                       ↓
              SQLite Database Layer
          (Historical Price Storage)
                       |
                       ↓
          Time-Series Forecasting Model
                (Facebook Prophet)
                       |
                       ↓
          Analytics & Risk Monitoring
                       |
                       ↓
          Streamlit Intelligence Dashboard
                       |
                       ↓
          Automated Email Price Alerts
</pre>

<hr>

<h2 id="datapipeline">5. Data Engineering Pipeline</h2>

<h3>5.1 Data Collection (Web Scraping)</h3>

<p>The system automatically extracts commodity prices from online market sources.</p>

<p>Tracked materials:</p>

<table border="1" cellpadding="5">
    <tr>
        <th>Commodity</th>
        <th>Application in Electrolyzer Systems</th>
    </tr>
    <tr>
        <td>Lithium Carbonate</td>
        <td>Battery and energy storage supply chain</td>
    </tr>
    <tr>
        <td>Copper</td>
        <td>Electrical components and current collectors</td>
    </tr>
    <tr>
        <td>Soda Ash</td>
        <td>Chemical processing applications</td>
    </tr>
    <tr>
        <td>Caustic Soda</td>
        <td>Electrochemical processes</td>
    </tr>
</table>

<p>Technology:</p>
<ul>
    <li>Python Requests</li>
    <li>BeautifulSoup</li>
    <li>Automated extraction workflow</li>
</ul>

<h3>5.2 Data Processing and Standardization</h3>

<p>Raw scraped information is converted into structured datasets.</p>

<p>Processing steps:</p>
<ul>
    <li>Date normalization</li>
    <li>Price conversion</li>
    <li>Missing value handling</li>
    <li>Data formatting</li>
    <li>Source tracking</li>
</ul>

<p>Example database structure:</p>

<table border="1" cellpadding="5">
    <tr>
        <th>Column</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Commodity</td>
        <td>Material name</td>
    </tr>
    <tr>
        <td>Date</td>
        <td>Market date</td>
    </tr>
    <tr>
        <td>Price</td>
        <td>Commodity price</td>
    </tr>
    <tr>
        <td>Currency</td>
        <td>CAD</td>
    </tr>
    <tr>
        <td>Source</td>
        <td>Data provider</td>
    </tr>
    <tr>
        <td>Scraped_at</td>
        <td>Collection timestamp</td>
    </tr>
</table>

<hr>

<h2 id="database">6. Database Management</h2>

<p>A lightweight SQLite database was implemented for local data management.</p>

<h3>Commodity Price Table</h3>
<p>Stores historical market information:</p>

<pre>
CREATE TABLE commodity_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    commodity TEXT NOT NULL,
    date TEXT NOT NULL,
    price REAL NOT NULL,
    currency TEXT DEFAULT 'CAD',
    source TEXT,
    scraped_at TEXT);
</pre>

<h3>Alert Table</h3>
<p>Stores generated procurement warnings:</p>

<pre>
CREATE TABLE alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    commodity TEXT,
    alert_type TEXT,
    message TEXT,
    created_at TEXT);
</pre>

<p>Advantages:</p>
<ul>
    <li>Fast local storage</li>
    <li>Easy deployment</li>
    <li>Reproducible analysis</li>
    <li>SQL-based querying capability</li>
</ul>

<hr>

<h2 id="forecasting">7. Time-Series Forecasting</h2>

<h3>Prophet Forecasting Model</h3>

<p>Historical commodity prices are analyzed using Facebook Prophet.</p>

<p>The model provides:</p>
<ul>
    <li>Future price prediction</li>
    <li>Trend identification</li>
    <li>Seasonal pattern analysis</li>
    <li>Confidence intervals</li>
</ul>

<p>Forecast outputs:</p>
<ul>
    <li>Predicted price</li>
    <li>Upper confidence limit</li>
    <li>Lower confidence limit</li>
</ul>

<p>Performance metrics:</p>
<ul>
    <li>RMSE (Root Mean Square Error)</li>
    <li>R² score</li>
</ul>

<p>Example workflow:</p>

<pre>
df_prophet = df[['date', 'price']].copy()
df_prophet.columns = ['ds', 'y']

model = Prophet(
    daily_seasonality=False,
    weekly_seasonality=True,
    yearly_seasonality=True)
model.fit(df_prophet)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
</pre>

<hr>

<h2 id="alerts">8. Intelligent Price Alert System</h2>

<p>The platform includes an automated monitoring system.</p>

<p>Users can define:</p>
<ul>
    <li>Commodity</li>
    <li>Price threshold</li>
    <li>Alert condition</li>
</ul>

<p>Example:</p>

<pre>
Lithium Carbonate Price > 5000 CAD
         ↓
   Generate Warning
         ↓
Send Email Notification
</pre>

<p>Benefits:</p>
<ul>
    <li>Prevent unexpected procurement costs</li>
    <li>Support purchasing decisions</li>
    <li>Enable proactive supply-chain management</li>
</ul>

<hr>

<h2 id="dashboard">9. Interactive Streamlit Dashboard</h2>

<p>The application provides multiple modules:</p>

<h3> Dashboard</h3>
<p>Provides:</p>
<ul>
    <li>Total database records</li>
    <li>Latest prices</li>
    <li>Commodity trends</li>
    <li>Interactive visualization</li>
</ul>

<h3> Data Scraping</h3>
<p>Features:</p>
<ul>
    <li>One-click market data collection</li>
    <li>Automatic database update</li>
</ul>

<h3> Forecast Module</h3>
<p>Provides:</p>
<ul>
    <li>Commodity selection</li>
    <li>Forecast horizon control</li>
    <li>Prediction visualization</li>
    <li>Model evaluation metrics</li>
</ul>

<h3> Email Alert Module</h3>
<p>Provides:</p>
<ul>
    <li>Threshold monitoring</li>
    <li>Alert generation</li>
    <li>Notification workflow</li>
</ul>

<h3> Database Management</h3>
<p>Features:</p>
<ul>
    <li>Data exploration</li>
    <li>Export CSV</li>
    <li>Historical record cleaning</li>
</ul>

<h3> Analytics Module</h3>
<p>Includes:</p>
<ul>
    <li>Price statistics</li>
    <li>Market changes</li>
    <li>Distribution analysis</li>
</ul>

<hr>

<h2 id="techstack">10. Technical Stack</h2>

<h3>Programming</h3>
<ul>
    <li>Python</li>
</ul>

<h3>Data Engineering</h3>
<ul>
    <li>Pandas</li>
    <li>SQLite</li>
    <li>SQL</li>
</ul>

<h3>Web Data Collection</h3>
<ul>
    <li>Requests</li>
    <li>BeautifulSoup</li>
</ul>

<h3>Machine Learning / Forecasting</h3>
<ul>
    <li>Facebook Prophet</li>
    <li>Time-Series Modeling</li>
</ul>

<h3>Visualization</h3>
<ul>
    <li>Plotly</li>
    <li>Streamlit</li>
</ul>

<h3>Database</h3>
<ul>
    <li>SQLite</li>
</ul>

<hr>

<h2 id="repository">11. Repository Structure</h2>

<pre>
Electrolyzer-Procurement-Intelligence/
│
├── app.py                          # Main Streamlit application
├── commodity_prices.db             # SQLite database
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── data/
│   └── historical_prices.csv       # Exported historical data
│
├── modules/
│   ├── scraping.py                 # Web scraping functions
│   ├── database.py                 # Database operations
│   ├── forecasting.py              # Prophet forecasting
│   ├── alerts.py                   # Email alert system
│   └── analytics.py                # Analytics functions
│
├── notebooks/
│   └── forecasting_analysis.ipynb  # Jupyter notebook for analysis
│
└── images/
    └── dashboard.png               # Dashboard screenshot
</pre>

<hr>

<h2 id="outcomes">12. Key Outcomes</h2>

<p>This project demonstrates an integrated engineering data platform capable of:</p>

<table border="1" cellpadding="5">
    <tr>
        <td>✅ Automated commodity data acquisition</td>
    </tr>
    <tr>
        <td>✅ Structured SQL database development</td>
    </tr>
    <tr>
        <td>✅ Real-time market monitoring</td>
    </tr>
    <tr>
        <td>✅ Predictive price forecasting</td>
    </tr>
    <tr>
        <td>✅ Procurement risk analysis</td>
    </tr>
    <tr>
        <td>✅ Interactive business intelligence dashboard</td>
    </tr>
</table>

<hr>

<h2 id="impact">13. Engineering Impact</h2>

<p>By combining:</p>

<p><b>Chemical Engineering + Data Engineering + Machine Learning</b></p>

<p>this platform supports smarter decision-making for electrolyzer commercialization.</p>

<p>The system provides a foundation for future integration with:</p>

<ul>
    <li>Electrolyzer cost models</li>
    <li>Digital twins</li>
    <li>AI-based procurement optimization</li>
    <li>Supply-chain risk prediction</li>
</ul>

<h3>Economic Impact</h3>

<table border="1" cellpadding="5">
    <tr>
        <th>Parameter</th>
        <th>Estimated Savings</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Material Cost Optimization</td>
        <td>10-20%</td>
        <td>Strategic timing of purchases</td>
    </tr>
    <tr>
        <td>Risk Reduction</td>
        <td>15-25%</td>
        <td>Early warning for price spikes</td>
    </tr>
    <tr>
        <td>Inventory Planning</td>
        <td>10-15%</td>
        <td>Forecast-based inventory management</td>
    </tr>
    <tr>
        <td>Scale-Up Cost Estimation</td>
        <td>15-30%</td>
        <td>Accurate material cost projections for 25 cm² scale-up</td>
    </tr>
</table>

<hr>

<h2 id="future">14. Future Improvements</h2>

<p>Future development opportunities:</p>

<ol>
    <li><b>Database Upgrade:</b> Replace SQLite with PostgreSQL/MySQL for industrial deployment</li>
    <li><b>Additional Data Sources:</b> Add more commodity APIs and market data providers</li>
    <li><b>Advanced Forecasting:</b> Implement LSTM/Transformer models for improved accuracy</li>
    <li><b>Cost Integration:</b> Add cost prediction for electrolyzer manufacturing</li>
    <li><b>Degradation Modeling:</b> Integrate catalyst degradation and material consumption models</li>
    <li><b>Cloud Deployment:</b> Deploy cloud-based monitoring with real-time updates</li>
    <li><b>User Management:</b> Multi-user access with role-based permissions</li>
    <li><b>Mobile Alerts:</b> SMS and push notifications for critical price alerts</li>
</ol>





