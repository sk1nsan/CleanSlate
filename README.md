# CleanSlate

**CleanSlate** is a tool designed to help users reclaim their online privacy by effortlessly removing digital footprints. With Cleanslate, you can delete posts and comments across multiple social media platforms, ensuring your online presence reflects your current values and preferences. Take control of your digital identity and enjoy peace of mind by managing what you share online.

---
## Installation

To run this project locally, follow these steps:

### Clone the Repository:
```bash
git clone https://github.com/sk1nsan/CleanSlate 
cd CleanSlate 
```

### Install Dependencies:
Make sure you have Python 3.x installed. Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables:
Create a `.env` file in the root directory and add the following:
```bash
CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_client_secret
```

### Run the Application:
```bash
python web_app/app.py
```

The app will run locally on `http://127.0.0.1:8080/`.

---

## Usage

1. **Get Started**: On the index page, click the "Get Started" button to navigate to the services page.

2. **Select Platform**: Choose the social media platform from which you want to delete your content.

3. **Authorize Access**: After selecting a platform, you’ll be redirected to authorize the request. Grant the necessary permissions to proceed.

4. **Set Date**: Select a date; all content prior to this date will be marked for deletion.

5. **Preview Content**: You will be redirected to a preview page where you can review all posts and comments scheduled for deletion based on the date you provided.

6. **Confirm Deletion**: Finally, confirm your deletion to complete the process.

---

## Contributing

If you would like to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request, describing the changes you have made and their significance.

---

## Licensing

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it according to the terms of the license.

---

### Author

- **Omar Ahmed**     - Backend Developer
- **Abdullah Ahmed** - Frontend Developer
