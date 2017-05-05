echo "./cdi -c cdi.js"
./cdi -c cdi.js &

sleep 3
echo "chmod 777 cdi-fcgi-socket"
chmod ugoa+rwx /tmp/cdi-fcgi-socket

echo "runing.............[Ok]"
