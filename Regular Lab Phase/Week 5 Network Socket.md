# Week 5 Mon Network Socket

---------------
#### :dizzy: **Lab Date :** Feb 9 Monday
#### :alarm_clock: **Due Date :** 2:00 pm Feb 16 (next Monday)   
#### :pencil: Every group member must be present for every check point.
-------------------

> [!NOTE]  
> Today’s lab requires your group to **frequently collaborate with another group** (the neighbor group seated next to you).

## 1. HTTP server — Static file host
- [ ] **Get your laptop and Pi both connected to the iot_lab WiFi**

In your laptop and Pi, use Terminal commands to get IP addresses of both devices.

- [ ] **A folder to host static files**

In your Pi, create a folder. Place some files into the folder, such as docs, pictures, videos.

In the Pi terminal

```shell
cd /path/to/your/folder
python3 -m http.server 8000
```

Here, the `http.server` is a module in the Python Standard Library. Its detailed usage in Terminal can be found in https://docs.python.org/3/library/http.server.html#command-line-interface

- [ ] **Access yours Pi server from your laptop**

In your laptop, open a browser, enter such address

```
http://<your_pi_ip>:8000
```

You should be able to access and download files from the folder.

Observe what happened on the Pi Terminal at the same time.

- [ ] **Access your neighbor's Pi server from your laptop**

In your laptop, also try to access your neighbro's server via browswer.

- [ ] Once done, stop the http server in your Pi Terminal.


----------


🎉 **Check Point 2**
<br>Each student will show the basic operations to the lab staff.

