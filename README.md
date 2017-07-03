# vagrant-docker-nginx
vagrant file to build ubuntu docker host and one container running nginx:alpine

To build this run (asuming you have an internet connection! )

```
$ vagrant up
```

Navigate to this [http://localhost:18080/]( http://localhost:18080 ) to verify the deployment has worked as expected.

You should see

# Hello world!


To verify the container has initialised correctly run

```
$ ./test.py

```


You should see as expected result of

```

We got an HTML response!
<H1>Hello World!</H1>
```

TODO:

Serverspec tests