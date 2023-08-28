# DotNetPerfMonitor Web Application

## Overview

DotNetPerfMonitor is a web application built using Nuxt3, TypeScript and VueJS that provides a user-friendly dashboard for visualizing the results of benchmark tests recorded in CSV files. The dashboard is deployed to Github Actions via a CDI/CD workflow that runs on PR merge.

## Project Structure

The project follows a standard Nuxt3 project structure. Here's an overview of the main directories and files:

- `public`: This directory contains static assets such as images icons, or font files.
- `components`: Contains reusable VueJS components used throughout the application.
- `composables`: Contains Nuxt3-styled utils functions used in the project.
- `layouts`: Defines the layout structure of the application pages.
- `pages`: Contains the application's pages and their corresponding Vue components.
- `plugins`: Includes JavaScript plugins that are automatically registered with the application.
- `static`: Stores static files that are served directly by the web server.
- `nuxt.config.js`: Configuration file for Nuxt3, where you can define plugins, modules, build settings, etc.
- `package.json`: Lists the project's dependencies and scripts.

## Getting Started

To run the DotNetPerfMonitor web application locally, follow these steps:

1. Clone the repository:

   ````shell
   git clone https://github.com/G-Research/DotnetPerfMonitor.git
   ```

1. Change into the project's directory:

   ````shell
   cd DotnetPerfMonitor/_dashboard
   ```

1. Install the dependencies:

   ````shell
   pnpm install
   ```

1. Start the development server:

   ````shell
   pnpm run dev
   ```

1. Open your web browser and visit `http://localhost:3000` to access the application.

## Contributing

We welcome contributions from the community to enhance the DotNetPerfMonitor web application. If you're interested in contributing, please follow these guidelines:

- Fork the repository on GitHub.

- Create a new branch for your feature or bug fix:

   ````shell
   git checkout -b my-feature
   ```

- Make your changes and ensure they adhere to the project's coding style and guidelines.

- Test your changes thoroughly to verify they work as expected.

- Commit your changes with descriptive commit messages:

   ````shell
   git commit -m "Add new feature: blablabla"
   ```

- Push your changes to your forked repository:

   ````shell
   git push origin my-feature
   ```


- Open a pull request on the main repository, explaining the purpose of your changes and providing any additional information that may be relevant.

- Be open to feedback and address any review comments or change requests.
