# Aether: Mission Control for the FINCH Satellite

Welcome to Aether, the mission control software for the University of Toronto Aerospace Team's FINCH mission. This README will guide you through the setup, usage, and customization of the Aether interface, built on the Open MCT platform, for the FINCH Mission Control Center team.

"To the stars – with friends!"


## Introduction


Aether is a web-based platform for mission operations data visualization and control, designed for the University of Toronto Aerospace Team's FINCH mission.  Leveraging Open MCT, Aether provides a robust interface for real-time telemetry visualization, command and control capabilities, and system status management.


## Prerequisites

Before you begin, ensure you have met the following requirements:
- Node.js (version 12 or later)
- npm (Node Package Manager)
- Git
- Access to satellite telemetry and command interfaces (API endpoints, data streams, etc.)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/aether-fincc-mission.git
   cd aether-fincc-mission
   
 2. **Install Dependencies:**
    
      ```bash
    npm install 
    
 3.**Run the Aether Application:**
  
    npm start

Open your browser(chrom) and navigate to http://localhost:8080 to access the Aether interface.

## Configuration

1.**Telemetry Data Sources:**

Configure your telemetry data sources by editing the src/telemetry/sources.js file.
Add your data streams, specifying the necessary parameters (URL, data format, etc.).

2.**Command Interface:**

Set up the command interface by editing src/commands/interface.js.
Ensure commands are properly formatted and accessible.

3.**perational Modes:**

Define and configure different operational modes for the FINCH mission in src/modes/operations.js.
Each mode should include specific parameters and telemetry requirements.

4.**Custom Plugins:**

To add custom plugins, create new JavaScript modules in the src/plugins/ directory.
Register the plugins in the src/plugins/index.js file.

## Usage
1.**Telemetry Visualization:**

Access real-time telemetry data through the provided panels and displays.
Customize views to include graphs, charts, and tables of key metrics.

2.**Command and Control:**

Send commands to the satellite using the command interface.
Monitor the status and response of issued commands.

3.**Operational Modes:**

Switch between different operational modes based on mission requirements.
Ensure all relevant telemetry data and commands are available for each mode.

4.**Historical Data Analysis:**

View historical telemetry data to analyze trends and performance over time.
Export data for offline analysis if needed.

## Customization
1.**Modify Layouts:**

Use the Open MCT layout editor to create custom dashboards tailored to the FINCH mission needs.
Save and share layouts with your team.

2.**Develop New Plugins:**

Extend Aether functionality by developing custom plugins.
Refer to the Open MCT Plugin Development Guide for more details.
