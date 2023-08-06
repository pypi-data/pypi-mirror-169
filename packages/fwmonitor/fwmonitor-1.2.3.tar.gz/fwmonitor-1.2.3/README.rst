FWMonitor
=========

``fwmonitor`` can be used to grok ``IPTABLES``, ``UFW`` or any program
that logs similar to ``IPTABLES``, logs from your ``syslog`` (*active*)
or a gathered log/text file (*passive*) in a comprehensive format in
order to conduct network traffic analysis and security audit of your
servers.

Demo
----

fwmonitor

Usage
-----

Install from ``PIP``:

.. code:: bash

   pip3 install fwmonitor

Or clone this repository:

.. code:: bash

   git clone https://github.com/pouriyajamshidi/fwmonitor.git

Make the script executable:

.. code:: bash

   chmod +x fwmonitor.py

For your convenience, you can place the program in your system PATH,
like ``/bin/`` or ``/usr/local/bin/`` for instance:

.. code:: bash

   sudo cp fwmonitor.py /usr/local/bin/fwmonitor

--------------

Flags
-----

This script takes 4 optional arguments. These arguments are:

**``--file``**: Location of log file to be scanned. Default location is
**/var/log/syslog**

**``--key``** : Keyword that ``IPTABLES`` uses to log events. Make sure
of case-sensitivity and specific keyword in your log file. Default value
for keyword is **“UFW BLOCK”**

**``--interval``**: Interval to read the log file from scratch, this is
useful for analyzing a live system. If you pass ``0`` here, it’ll scan
the log file once and exits. Default value for interval is **60
seconds**

**``--ipv6``**: Display ``IPv6`` logs. Default is **IPv4**

**``--version``**: Display version and exit

*By running the script without providing any arguments, the default
values as mentioned below above be used.*

Examples
--------

To analyze a log file that you have gathered:

.. code:: python

   fwmonitor --file mytraffic.log --key "IPTABLES_BLOCK" --interval 0
   # OR
   python3 fwmonitor.py --file mytraffic.log --key "IPTABLES_BLOCK" --interval 0

Audit a live server:

.. code:: python

   fwmonitor --file /var/log/syslog --key "IPTABLES_BLOCK"
   # OR
   python3 fwmonitor.py --file /var/log/syslog --key "IPTABLES_BLOCK"

Additionally, there is a ``sample.log`` in this repository that you can
utilize to see how this script works without actually having a log file
yourself. Use it like:

.. code:: bash

   fwmonitor --file sample.log --key "UFW BLOCK" --interval 0
   # OR
   python3 fwmonitor.py --file sample.log --key "UFW BLOCK" --interval 0

Tested on
---------

Ubuntu.

*It can be used on ``Windows`` and ``Mac OS`` as well to analyze the
gathered log file(s).*


Contributing
------------

Pull requests are welcome.

License
-------

`License: MIT <https://opensource.org/licenses/MIT>`__
