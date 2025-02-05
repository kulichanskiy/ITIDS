# ITIDS (Intelligent Transit Information Display System)

## Project Overview
ITIDS is an innovative system designed to provide real-time transit information through intelligent display units located within public transportation systems such as subways, buses, and trains. This system aims to improve the passenger experience by displaying important information like station names, arrival times, transfers, and more, while integrating additional features such as advertising space. The system utilizes the structure of the Vancouver Metro system, which is managed by TransLink, as its foundational layout for station and route data.

## Features
- **Real-time Transit Information:** Displays upcoming station names, arrival times, and connecting transport services.
- **Multimedia Support:** Includes space for advertisements and visual content to enhance user engagement.
- **Accessibility:** Designed with accessibility in mind, ensuring that individuals with disabilities can easily access the information.
- **Data Storage & Management:** A robust database for managing station and route data, allowing for easy updates and maintenance.
- **Scalable Architecture:** The system can be deployed in any transit system and scaled as needed, with support for the TransLink network in Vancouver as a starting point.

## Technical Specifications
- **Frontend:**
  - **Technologies Used:** HTML, CSS, JavaScript (ES6+)
  - **Features:**
    - Interactive and user-friendly interface.
    - Real-time data fetching and display.
    - Responsive design for various screen sizes, including high-resolution displays.
- **Backend:**
  - **Technologies Used:** Python (Flask), SQL (SQLite)
  - **Features:**
    - RESTful API for fetching and updating transit data.
    - Connection to a local database for storing and managing transit-related data.
    - Webhooks for integrating with external systems like Telegram for notifications.
- **Database:**
  - **Technologies Used:** SQLite
  - **Tables:**
    - **Stations:** Stores details of transit stations, with data based on the TransLink Vancouver Metro network.
    - **Routes:** Information about different routes available within the Vancouver Metro system and beyond.
    - **Connections:** Stores data on transfers between different modes of transport.
    - **Advertisements:** Handles advertisement data, allowing them to be displayed dynamically.

## System Architecture
The system follows a modular architecture, making it easy to integrate new features or expand it to other regions. Key components of the architecture include:
- **Data Source Layer:** Data from local transit authorities (like TransLink) and third-party APIs.
- **Backend Layer:** Manages data processing, storage, and APIs for frontend communication.
- **Frontend Layer:** Displays data and provides real-time interaction with users.

## Installation Guide
### Prerequisites
- Python 3.7+  
- Flask
- SQLite
- JavaScript-enabled browser

### Steps to Install
WIP

## How It Works

### Data Flow
1. **Backend Fetching Data:**
   - The backend retrieves transit data either from external APIs or local data files, including station and route information from the Vancouver Metro system, as structured by TransLink.
   - This data is then processed and stored in an SQLite database for efficient access.

2. **Displaying Information:**
   - The frontend fetches the data from the backend via API calls, dynamically displaying real-time transit information on the display screens within transit stations or vehicles.
   - This includes upcoming station names, arrival times, transfer details, and any additional multimedia content like advertisements.

3. **User Interaction:**
   - Passengers interact with the system through large, high-resolution displays. They can view real-time updates about station arrivals, transfers, and next routes.
   - The system also supports multimedia content, allowing for advertisements or other information to be displayed alongside the transit details.

### Advertisement Display
Alongside the transit information, the system can dynamically show advertisements:
- **Advertisement:** “Discount tickets available for the next week. Visit our website for more details!”
- **Advertisement Duration:** Displayed for 30 seconds before the next transit update.

## Future Enhancements
- **Integration with GPS systems:** Real-time location tracking for buses and trains to provide more accurate arrival times.
- **Advanced Accessibility Features:** Implement text-to-speech capabilities, making the system more accessible for individuals with visual impairments.
- **Cloud Integration:** Migrate the backend database to a cloud platform for better scalability and regional expansion.
- **Multi-language Support:** Add multiple language options to cater to a broader range of passengers and improve accessibility in diverse regions.

## Contributing
We welcome contributions to improve ITIDS! If you find any issues or have new feature ideas, please submit a pull request or open an issue in the GitHub repository.

### How to Contribute:
1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes and push them to your branch.
4. Open a pull request to submit your contributions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

   
