# Image Watermarking: GUI Desktop Application with Python and Tkinter

Welcome to the Image Watermarking repository, a GUI desktop application developed using Python and its Tkinter library. This project offers a seamless solution for watermarking images, allowing users to upload their desired image, input a custom text, and have that text elegantly watermarked onto the image. The application provides a user-friendly interface where you can easily perform this task and save the watermarked image directly to your system's Pictures folder. Whether you want to protect your creative work or add a personalized touch to your images, the Image Watermarking desktop application provides a convenient and efficient solution. Enhance your image editing capabilities with this easy-to-use GUI application and start watermarking images with precision and style.

<b>
  <a href='https://ishanrastogi26.wordpress.com/2023/07/02/hello-world/'>
    Click to View the Complete Step-by-Step Guide to Building this Project.
  </a>
</b>

<h1> Summary of Guide to Building this Project </h1>

<h2> Step 1: Setting up Screen </h2>
<p>
  Import the Tkinter library and create a window object using <em>Tk()</em>. Then call <em>mainloop()</em> method to keep the window on unless closed by the user.
</p>


<h2> Step 2: Setting up Widgets </h2>
<p>
  We use the canvas widget to create a background. We first set up its size equal to the image dimensions. Create a usable image using <em> PhotoImage() </em>. 
  Then we use <em> create_image </em> and <em> create_text </em> to display an image and text for good UI. 
  We create an input field and two buttons for uploading images and submit button. We use <em> grid </em> layout to display our widgets in a systematic matter.
</p>


<h2> Step 3: Defining Methods of Buttons </h2>
<p>
  We first define a method for the <em> Upload </em> button. We use <em>filedialog.askopenfilename</em> method of tkinter to open a dialogue box to ask the user to upload the file.
  Then we save its name and display the name on the screen and make <em> Upload </em> button text green to show the file as uploaded. 
  The uploaded file path is saved in a global variable passed to the method of submit button. <br>
</p>


<h2> Step 4: Watermarking the Image and Saving it </h2>
<p>
  We need the pillow library to watermark our image. Pillow is a library for <em>Image Processing</em>. 
  We use three objects from it, <em>Image, ImageDraw, and ImageFont.</em> 
  We create a new image with the same dimensions as the older one and write a piece of text on it with a defined colour code. 
  Then we save it and show it to the user.
  After that, we reset the widgets to make them look ready to take another input.
</p>
