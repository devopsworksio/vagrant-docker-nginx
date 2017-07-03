# vagrant-docker-nginx
vagrant file to build ubuntu docker host and one container running nginx:alpine

To build this run (asuming you have an internet connection! )

```
$ vagrant up
```

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