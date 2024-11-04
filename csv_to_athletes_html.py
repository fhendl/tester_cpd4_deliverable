import csv

def process_athlete_data(file_path):

   # Extracting athlete stats by year
   records = []

   # Extracting athlete races
   races = []           

   athlete_name = ""
   athlete_id = ""
   comments = ""

   with open(file_path, newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      data = list(reader)

      athlete_name = data[0][0]
      athlete_id = data[1][0]
      print(f"The athlete id for {athlete_name} is {athlete_id}")

      for row in data[5:-1]:
         if row[2]:
            records.append({"year": row[2], "sr": row[3]})
         else:
            races.append({
               "finish": row[1],
               "time": row[3],
               "meet": row[5],
               "url": row[6],
               "comments": row[7]
            })

   return {
      "name": athlete_name,
      "athlete_id": athlete_id,
      "season_records": records,
      "race_results": races,
      "comments": comments
   }    

def gen_athlete_page(data, outfile):
   # template 
   # Start building the HTML structure
   html_content = f'''<!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <!-- Get your own FontAwesome ID -->
       <script src="https://kit.fontawesome.com/YOUR_ID.js" crossorigin="anonymous"></script>

      <link rel="stylesheet" href="../css/reset.css">
      <link rel="stylesheet" href="../css/style.css">

      <title>{data["name"]}</title>
   </head>
   <body class="light-mode">
   <a href = "#main">Skip to Main Content</a>
   <nav>
     <ul>
        <li><a href="index.html">Home Page</a></li>
        <li><a href="mens.html">Men's Team</a></li>
        <li><a href="womens.html">Women's Team</a></li>
     </ul>
   </nav>

   <button id="mode-toggle">Light Mode (Click Twice)</button>
   <button id="high-contrast-toggle">Dark Mode</button>

   <header>
      <!--Athlete would input headshot-->
       <h1>{data["name"]}</h1>
      <img src="../images/profiles/{data["athlete_id"]}.jpg" alt="Athlete headshot" width="200"> 
   </header>
   <main id = "main">
      <section id= "athlete-sr-table">
         <h2>Athlete's Seasonal Records (SR) per Year</h2>
            <table>
                  <thead>
                     <tr>
                        <th> Year </th>
                        <th> Season Record (SR)</th>
                     </tr>
                  </thead>
                  <tbody>
                  '''
   
   for sr in data["season_records"]:
      sr_row = f'''
                     <tr>
                        <td>{sr["year"]}</td>
                        <td>{sr["sr"]}</td>
                     </tr>                  
               '''
      html_content += sr_row

   html_content += '''                   
                </tbody>
                  </table>
                     </section>

                        <h2>Race Results</h2>

                        <section id="athlete-result-table">
                           

                           <table id="athlete-table">
                              <thead>
                                 <tr>
                                    <th>Race</th>
                                    <th>Athlete Time</th>
                                    <th>Athlete Place</th>
                                    <th>Race Comments</th>
                                 </tr>
                              </thead>

                              <tbody>
                  '''

   # add each race as a row into the race table 
   for race in data["race_results"]:
      race_row = f'''
                                 <tr class="result-row">
                                    <td>
                                       <a href="{race["url"]}">{race["meet"]}</a>
                                    </td>
                                    <td>{race["time"]}</td>
                                    <td>{race["finish"]}</td>
                                     <td>{race["comments"]}</td>
                                 </tr>
      '''
      html_content += race_row

   html_content += '''
                              </tbody>

                        </table>
                     </section>
                     <section id = "gallery">
                     <h2>Gallery</h2>
                     <a href="#" id="open-gallery">Click here to view the gallery</a>
                     <div id="gallery-container"></div> <!-- Container for the images -->
                      </section>
                     </main>
                     <footer>
                     <p>
                     Skyline High School<br>
                     <address>
                     2552 North Maple Road<br>
                     Ann Arbor, MI 48103<br><br>

                    <a href="https://www.instagram.com/a2skylinexc/" aria-label="Follow us on Instagram">
                        <i class="fa-brands fa-instagram"></i> Follow us on Instagram </a>


                     </footer>
<!-- JavaScript for Light/Dark Mode, High Contrast Mode, and Gallery -->
<script>
   document.getElementById('mode-toggle').addEventListener('click', function() {
      if (document.body.classList.contains('dark-mode')) {
         document.body.classList.remove('dark-mode');
         document.body.classList.add('light-mode');
         document.getElementById('mode-toggle').innerText = 'Dark Mode';
      } else {
         document.body.classList.remove('light-mode');
         document.body.classList.add('dark-mode');
         document.getElementById('mode-toggle').innerText = 'Light Mode (Click Twice)';
      }
   });

   document.getElementById('high-contrast-toggle').addEventListener('click', function() {
      document.body.classList.toggle('high-contrast-mode');
      document.body.classList.remove('dark-mode'); /* Reset dark mode */
      document.body.classList.remove('light-mode'); /* Reset light mode */
      document.getElementById('mode-toggle').innerText = 'Dark Mode';
   });

   // JavaScript for loading gallery images dynamically
   document.getElementById('open-gallery').addEventListener('click', function() {
      // Show the gallery section
      document.getElementById('gallery').style.display = 'block';
      
      // Target container for gallery images
      const galleryContainer = document.getElementById('gallery-container');

      // Clear the gallery container before loading new images
      galleryContainer.innerHTML = '';

      // List of folders inside 'gallery_images'
      const folders = ['235827', '236072', '236875', '238311', '943367', '947091'];

      // Base path to gallery_images folder
      const basePath = '../gallery_images/';  // Adjust path based on your folder structure

      // Loop through each folder and load images
      folders.forEach(folder => {
          const folderPath = basePath + folder + '/';
          
          // Dynamically add image elements
          for (let i = 1; i <= 5; i++) {  // Assuming 5 images per folder
              const img = document.createElement('img');
              img.src = folderPath + `image${i}.jpg`; // Adjust filename pattern if necessary
              img.alt = `Image ${i} from folder ${folder}`;
              img.classList.add('gallery-image');
              galleryContainer.appendChild(img);
          }
      });
   });
</script>

               </body>
         </html>
   '''

   with open(outfile, 'w') as output:
      output.write(html_content)
