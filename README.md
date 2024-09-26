<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">STGen: A Sensor Traffic Generator for IoT Protocol Verification and Evaluation </h3>

  
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## Getting Started

The STGen IoT sensor traffic generator is a publisher/subscriber model. It generates the random sensor data and creates a virtual system environment to simulate the data transmission over the netwrok protocol.

### Prerequisite
<ol>
    <li> The operating system should be Linux to run the testbed.</li>
    <li> Python3 is also a prerequisite. You can check if python is intalled in your device or not by running the following command.</li>
    
```sh
    python3
```

</ol>




## Installation

1. Downnload the github repo or clone it using the following command.
```sh
    git clone https://github.com/MehrajRahman/STGen-Sensor-Traffic-Generator.git
```
2. Open cmd in your computer. Now change the directory to the downloaded codebase.

3. Run the following command
```sh
   cd launcher
```
4. Run make command. this will construct your launcher environment.
```sh
   python3 iot-launcher.py ../conf/test.conf localhost 5004 5005 10 4 1 -A
```
5. Open another terminal. change the directory to the downloaded file. Now run the follwing command.

```sh
   cd iot/application
```

6. Run the client.

```sh
   ./iotclient -lclient1_sensor_log -slocalhost -rgps_2  -p5005 -A
```

Now I beileve you are witnessing the whole system running and transmitting the data from server to client after generating the data.



## Contact
for any isues you can send mail to any of the following address:

<li>hasan.mahmood@ewubd.edu</li>
<li>rahmanmehraj627@gmail.com</li>
<p align="right">(<a href="#readme-top">back to top</a>)</p>