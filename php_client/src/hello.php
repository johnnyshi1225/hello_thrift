<?php 
$BASE_DIR = realpath(dirname(__FILE__));
$GLOBALS['THRIFT_ROOT'] = $BASE_DIR . '/thrift';

require_once $GLOBALS['THRIFT_ROOT'].'/Thrift.php';
require_once $GLOBALS['THRIFT_ROOT'].'/protocol/TBinaryProtocol.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TSocket.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/THttpClient.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TBufferedTransport.php';

require_once $GLOBALS['THRIFT_ROOT'] . '/packages/hello/UserManager.php';

try {

	$socket = new TSocket('localhost', 9876);
	$transport = new TBufferedTransport($socket, 1024, 1024);
	$protocol = new TBinaryProtocol($transport);
	$client = new UserManagerClient($protocol);

	$transport->open();

	# ping
	$client->ping();

	# add user
	$u = new hello_User();
	$u->user_id = 1;
	$u->firstname = 'John';
	$u->lastname = 'Smith';
	$u->sex = hello_SexType::MALE;
	if ($client->add_user($u)) {
		echo 'user added succesfully</br>';
	}
	
	var_dump($client->get_user(0));
	
	# clear list
	$client->clear_list();
	
	# add user
	$u2 = new hello_User();
	$client->add_user($u2);
	
} catch (hello_InvalidValueException $e) {
	echo $e->error_msg.'<br/>';
}

?>
