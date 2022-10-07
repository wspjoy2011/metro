<?php

$orderId = Order::getOrderId();
if ( empty($orderId)) {
	fURL::redirect('/');
}

$order = new Order($orderId);
$orderType = $order->getOrderType();
if ( $order->isCreditExtension() ) {
	// prepare order dependencies
	// product entity id = client credit id
	$credit = new ClientCredit( $order->getProductEntityId() );
	$credit_extension = Credit_Extension::get_record();

	$package_price = new PackagePrice( $credit->getPackagePricesId() );
	$package = new Package( $package_price->getPackagesId() );

	// prepare credit expiration timestamp and date to be displayed
	$credit_old_expiration_timestamp = strtotime( $credit->getExpiration()->format('Y-m-d H:i:s') );
	$credit_new_expiration_timestamp = strtotime( '+' . $credit_extension->getExpirationMonths() . ' months' );

	$credit_old_expiration_date = date( 'Y F d H:i:s', $credit_old_expiration_timestamp );
	$credit_new_expiration_date = date( 'Y F d H:i:s', $credit_new_expiration_timestamp );
} else if ( $order->isMiscSale() ) {

	// Do nothing, since this order type is not associated with any content

} else {
	$packagePrice = new PackagePrice($order->getPackagePriceId());
	$package = new Package($packagePrice->getPackagesId());
	$pricing = fRecordSet::build('PackagePrice', array('packages_id=' => $package->getId(), 'deleted=' => 0), array('credits' => 'asc', 'price' => 'asc'));
}

$client = Client::getClient();

if (fAuthorization::checkLoggedIn()) {
	$paymentProfiles = fRecordSet::build('ClientPaymentProfile', array('client_id=' => GlobalRegistry::get('client')->getAssociatedIds()));
}

$template->add('js', '/js/jquery-ui-1.12.1.min.js');


try {
    $return = $order->processInformation(true);
} catch (fNotFoundException $fnfex) { // if there's an fNotFound exception (most likely package price id related) just redirect to step 1
    Logger::write('fNotFound Exception: ' . $fnfex->getMessage(), __FILE__, __LINE__, $orderId);
    error_log('Billing fNotFound Exception line ' . __LINE__ . ': ' . $fnfex->getMessage());
    fURL::redirect('/');
}

if (fRequest::isPost()) {
	Logger::write("Redirecting user to " . $_SERVER['REQUEST_URI'], __FILE__, __LINE__, $orderId);
	fURL::redirect($_SERVER['REQUEST_URI']);
}

Logger::write("User entered step 3", __FILE__, __LINE__, $orderId);

/**
 * Checks if there is an already registered client with the current email
 * If true, checks if the client has made any past orders and if the current package
 * is for New Customers Only, redirects the client to Step 2
 */
if ( !fAuthorization::checkLoggedIn() ) {
	if ($client && $package->getNewCustomerOnly() && ( client_has_completed_orders($client) || is_current_user_email_restricted($client) ) ) {
		Logger::write("User kicked out after submitting final order: Product is for new customers only", __FILE__, __LINE__, $orderId);

		$errors_messages[] = array('message' => 'Sorry, this product is available for first time customers only. <br/>Feel free to start your order at the main order page.');
		fMessaging::create('error', '/order/step1', serialize($errors_messages));
		fURL::redirect('/start/');
	}
}

// Validate Step 1
if ( $order->isPackageOrder() ) {
	$errors = $order->validateStep1();

	if ($errors !== FALSE) {
		fMessaging::create('error', '/order/step1', serialize($errors));
		fURL::redirect('/start/');
	}
}

/*
 * Get information from Order object if it exists, if not
 * get it from the Client object. If neither exists oh well,
 * we tried.
 */
function getClientInfo($field) {
	global $order, $client;
	$method = 'get' . fGrammar::camelize($field, true);

	if ($order->$method()) {
		return $order->$method();
	} else if ($client->$method()) {
		return $client->$method();
	} else {
		return '';
	}
}

// This has been changed from show to retrieve because we need to log
// the error and it gets deleted when it gets shown or retrieved
$error = fMessaging::retrieve('error', '/order/');
if ($error) Logger::write("Server-side error occurred: " . strip_tags($error), __FILE__, __LINE__, $orderId);
//fMessaging::show('error', '/order/', 'form-message form-error'); // REMOVE ME WHEN READY FOR PRODUCTION //

if ($error) {
	?><p class="form-message form-error form-error-billing"><?php echo $error; ?></p><?php
}

if ($order->getOrderType() == 'credit-only' && $order->getWriting()) {
    $order->setWriting(0);
    $order->store();
}

echo $order->processError(2);
?>

<form id="order" method="post" action="/order/process/" class="form-section">
        <?php if ($orderType == 'misc-sale') : ?>
        <p style="margin-top: 20px;margin-bottom: 0;" class="total">Enter Amount To Be Charged: $ <a class="anchor" name="misc_sale_payment_amount"></a><input style="margin-left: -7px;width: 110px;" class="total" type="number" name="misc_sale_payment_amount" id="misc_sale_payment_amount" required value="<?php echo fSession::get('misc_sale_payment_amount'); ?>" pattern="[0-9]+(\.[0-9]{1,2})?" step="0.01" /></p>
        <?php else : ?>
	<h2 class="step-heading" style="margin: 30px 0px 10px 0px;">Step 3 of 3</h2>
        <?php endif; ?>
        <?php
        if ( $order->isPackageOrder() && ( $pricing->count() > 1 ) && ($order->getClientCreditsId() == NULL) ) {
                $baseCredits = $packagePrice->getBaseCredits();
                ?>
                <h2 style="font-size: 24px">Boost Results &amp; Lock In Savings</h2>
                <style>
                    .bigger_billing p {
                        font-size: 18px;
                        line-height: 20px;
                    }

                    label > span {
                        font-size: 16px !important;
                    }
                </style>
                <div class="bigger_billing"><p>One press release is not a PR campaign.</p>
            <p>Improve your PR visibility by sending multiple press releases to the
                media over coming months.</p>
            <p><em>Make a commitment now!</em></p>
                </div>

            <div class="order-step-3">
                <?php

                $flag = false;
                foreach ($pricing as $price) {
                    if (!$flag) {
                        $basePrice = $price->getPrice();
                    }
                    $flag = true;

                    if ( $price->getId() == $order->getPackagePriceId() ) {
                            $checked = " checked=\"checked\"";
                            $quantity = $price->getCredits();
                    } else {
                            unset($checked);
                    }

                    $writingService = '';

                    if ($price->getCredits() == $baseCredits) {
                        if ( $order->getWriting() ) {
                                $writingService = ' with Writing Service';
                                $actualPrice = $basePrice + ($price->getCredits() * $package->getWritingPrice());
                        } else {
                                $actualPrice = $basePrice;
                        }
                        echo '<div class="group-step"><input class="radio-upgrade" data-wprice="' . $package->getWritingPrice() . '" data-price="' . money_format('%.2n', $price->getPrice()) . '" data-credits="' . $price->getCredits() . '" type="radio" id="nocredit" name="package_price_id" value="' . $price->getId() . '"' . $checked . ' required />&nbsp;&nbsp;&nbsp;<label for="nocredit" style="font-size: 16px;">No additional PR submissions (' . money_format('%.2n', $actualPrice) . $writingService . ' - base price)</label></div><br />';
                    } else {
                        $verbage = null;
                        $bold = '';
                        if ($price->getCredits() === $packagePrice->getCredits()) {
                            $verbage = 'You have selected';
                            $bold = 'font-weight:bold;';
                        } else {
                            $verbage = ($price->getCredits() < $packagePrice->getCredits()) ? 'Downgrade to' : 'Upgrade to';
                        }
                        $savings = ((($price->getCredits() / $baseCredits) * $basePrice) - $price->getPrice());
                        $savingsText = ($savings > 0) ? '<span class="highlight">SAVE ' . money_format('%.2n', $savings) . '</span> ' : '';

                        echo '<div class="group-step"><input class="radio-upgrade" data-wprice="' . $package->getWritingPrice() . '" data-price="' . money_format('%.2n', $price->getPrice()) . '" data-credits="' . $price->getCredits() . '" type="radio" name="package_price_id" value="' . $price->getId() . '" id="' . $price->getId() . '"' . $checked . '>&nbsp;&nbsp;&nbsp;<label for="' . $price->getId() . '" style="font-size: 16px;' . $bold . '">' . $savingsText . '<span class="pkgVerbage">' . $verbage . '</span> a ' . $order->getPackageName() . ' ' . $price->getCredits() . ' pack';

                        // Make sure we calculate the additional writing cost and show that the additional credits have writing attached to them.
                        if ( $order->getWriting() ) {
                                echo ' including Writing Service';
                                $actualPrice = $price->getPrice() + ($price->getCredits() * $package->getWritingPrice());
                        } else {
                                $actualPrice = $price->getPrice();
                        }

                        echo ' (' . money_format('%.2n', ($actualPrice)) . ' - base price)' . '</label></div><br />' . PHP_EOL;
                    }
                }
                ?>
            </div>
                <p></p>
                <!-- <p class="note"><em>Note:</em> Remaining press release submissions can be used up to 12 months from time of order.</p> -->
                <?php
        }
        ?>

	<?php if ($order->getTotal() > 0 || $order->isMiscSale()) { ?>
		<div id="preview" class="column short" style="width:300px">
			<h2>Your Information</h2>

			<div id="your-info-wrap">
				<div class="form-row">
					<a class="anchor" name="first_name"><label for="first_name">First Name</label></a>
					<input type="text" data-nocounter="true" data-maxchar="50" name="first_name" id="first_name" required value="<?php echo getClientInfo('firstName') ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="last_name"><label for="last_name">Last Name</label></a>
					<input type="text" data-nocounter="true" data-maxchar="50" name="last_name" id="last_name" required value="<?php echo getClientInfo('last_name') ?>" />
				</div>

				<div class="form-row">
					<label for="company">Company</label>
					<input type="text" data-nocounter="true" data-maxchar="50" name="company" id="company" value="<?php echo getClientInfo('company') ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="email"><label for="email">E-Mail</label></a>
					<input type="text" data-nocounter="true" data-maxchar="255" name="email" id="email" required value="<?php echo getClientInfo('email') ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="address"><label for="address">Address</label></a>
					<input type="text" data-nocounter="true" data-maxchar="60" name="address" id="address" required value="<?php echo getClientInfo('address') ?>" />
				</div>

				<div class="form-row">
					<label for="address_2">Address 2</label>
					<input type="text" data-nocounter="true" data-maxchar="60" name="address_2" id="address_2" value="<?php echo getClientInfo('address2') ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="city"><label for="city">City</label></a>
					<input type="text" data-nocounter="true" data-maxchar="40" name="city" id="city" value="<?php echo getClientInfo('city') ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="state"><label for="state">State/Province</label></a>

					<select id="state" name="state" class="styledInput">
						<?php
						$current_status = getClientInfo('state') ? : 'Select State';
						$states = array('' => 'Select State', 'Other' => 'Other', 'AL' => "Alabama", 'AK' => "Alaska", 'AZ' => "Arizona", 'AR' => "Arkansas", 'CA' => "California", 'CO' => "Colorado", 'CT' => "Connecticut", 'DE' => "Delaware", 'DC' => "District Of Columbia", 'FL' => "Florida", 'GA' => "Georgia", 'HI' => "Hawaii", 'ID' => "Idaho", 'IL' => "Illinois", 'IN' => "Indiana", 'IA' => "Iowa", 'KS' => "Kansas", 'KY' => "Kentucky", 'LA' => "Louisiana", 'ME' => "Maine", 'MD' => "Maryland", 'MA' => "Massachusetts", 'MI' => "Michigan", 'MN' => "Minnesota", 'MS' => "Mississippi", 'MO' => "Missouri", 'MT' => "Montana", 'NE' => "Nebraska", 'NV' => "Nevada", 'NH' => "New Hampshire", 'NJ' => "New Jersey", 'NM' => "New Mexico", 'NY' => "New York", 'NC' => "North Carolina", 'ND' => "North Dakota", 'OH' => "Ohio", 'OK' => "Oklahoma", 'OR' => "Oregon", 'PA' => "Pennsylvania", 'RI' => "Rhode Island", 'SC' => "South Carolina", 'SD' => "South Dakota", 'TN' => "Tennessee", 'TX' => "Texas", 'UT' => "Utah", 'VT' => "Vermont", 'VA' => "Virginia", 'WA' => "Washington", 'WV' => "West Virginia", 'WI' => "Wisconsin", 'WY' => "Wyoming");
						foreach ($states as $key => $value) {
							fHTML::printOption($value, $key, $current_status);
						}
						?>
					</select>

					<label style="display:none" for="state">&nbsp;</label><input style="display:none" type="text" data-nocounter="true" data-maxchar="40" name="state_other" id="state_other" value="<?php echo $order->getState() ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="country"><label for="country">Country</label></a>

					<select id="country" name="country" style="width:190px" class="styledInput">
						<?php
						$current_status = getClientInfo('country') ? : 'United States';
						$countries = $db->query('SELECT printable_name FROM countries ORDER BY printable_name');
						foreach ($countries AS $country) {
							fHTML::printOption($country['printable_name'], $country['printable_name'], $current_status);
						}
						?>
					</select>
				</div>

				<div class="form-row">
					<a class="anchor" name="zip_code"><label for="zip_code">Zip Code</label></a>
					<input type="text" data-nocounter="true" data-maxchar="20" name="zip_code" id="zip_code" value="<?php echo getClientInfo('zip_code') ?>" />
				</div>
			</div>
		</div>

		<div class="column short" style="width:300px">
			<h2>Billing Information</h2>

			<div id="billing-info-wrap">
        <div class="form-chech"><input type="checkbox" id="billing_same" /><label for="billing_same">Billing information is the same</label></div>

				<div class="form-row">
					<a class="anchor" name="billing_first_name"><label for="billing_first_name">First Name</label></a>
					<input type="text" data-nocounter="true" data-maxchar="50" name="billing_first_name" id="billing_first_name" value="<?php echo _empty($order->getBillingFirstName()) ? $order->getFirstName() : $order->getBillingFirstName(); ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="billing_last_name"><label for="billing_last_name">Last Name</label></a>
					<input type="text" data-nocounter="true" data-maxchar="50" name="billing_last_name" id="billing_last_name" value="<?php echo _empty($order->getBillingLastName()) ? $order->getLastName() : $order->getBillingLastName(); ?>" />
				</div>

				<div class="form-row">
					<label for="billing_company">Company</label>
					<input type="text" data-nocounter="true" data-maxchar="50" name="billing_company" id="billing_company" value="<?php echo $order->getBillingCompany(); ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="billing_address"> <label for="billing_address">Address</label></a>
					<input type="text" data-nocounter="true" data-maxchar="60" name="billing_address" id="billing_address" value="<?php echo $order->getBillingAddress() ?>" />
				</div>

				<div class="form-row">
					<label for="billing_address_2">Address 2</label>
					<input type="text" data-nocounter="true" data-maxchar="60" name="billing_address_2" id="billing_address_2" value="<?php echo $order->getBillingAddress2() ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="billing_city"><label for="billing_city">City</label></a>
					<input type="text" data-nocounter="true" data-maxchar="40" name="billing_city" id="billing_city" value="<?php echo $order->getBillingCity() ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="billing_state"><label for="billing_state">State/Province</label></a>

					<select id="billing_state" name="billing_state" class="styledInput">
						<?php
						$current_status = $order->getBillingState() ? : 'Select State';
						$states = array('' => 'Select State', 'Other' => 'Other', 'AL' => "Alabama", 'AK' => "Alaska", 'AZ' => "Arizona", 'AR' => "Arkansas", 'CA' => "California", 'CO' => "Colorado", 'CT' => "Connecticut", 'DE' => "Delaware", 'DC' => "District Of Columbia", 'FL' => "Florida", 'GA' => "Georgia", 'HI' => "Hawaii", 'ID' => "Idaho", 'IL' => "Illinois", 'IN' => "Indiana", 'IA' => "Iowa", 'KS' => "Kansas", 'KY' => "Kentucky", 'LA' => "Louisiana", 'ME' => "Maine", 'MD' => "Maryland", 'MA' => "Massachusetts", 'MI' => "Michigan", 'MN' => "Minnesota", 'MS' => "Mississippi", 'MO' => "Missouri", 'MT' => "Montana", 'NE' => "Nebraska", 'NV' => "Nevada", 'NH' => "New Hampshire", 'NJ' => "New Jersey", 'NM' => "New Mexico", 'NY' => "New York", 'NC' => "North Carolina", 'ND' => "North Dakota", 'OH' => "Ohio", 'OK' => "Oklahoma", 'OR' => "Oregon", 'PA' => "Pennsylvania", 'RI' => "Rhode Island", 'SC' => "South Carolina", 'SD' => "South Dakota", 'TN' => "Tennessee", 'TX' => "Texas", 'UT' => "Utah", 'VT' => "Vermont", 'VA' => "Virginia", 'WA' => "Washington", 'WV' => "West Virginia", 'WI' => "Wisconsin", 'WY' => "Wyoming");
						foreach ($states as $key => $value) {
							fHTML::printOption($value, $key, $current_status);
						}
						?>
					</select>

					<label style="display:none" for="billing_state">&nbsp;</label><input style="display:none" type="text" data-nocounter="true" data-maxchar="40" name="billing_state_other" id="billing_state_other" value="<?php echo $order->getBillingState() ?>" />
				</div>

				<div class="form-row">
					<a class="anchor" name="billing_country"><label for="billing_country">Country</label></a>

					<select id="billing_country" name="billing_country" style="width:190px" class="styledInput">
						<?php
						$current_status = $order->getBillingCountry() ? : 'United States';
						$countries->seek(0);
						foreach ($countries AS $country) {
							fHTML::printOption($country['printable_name'], $country['printable_name'], $current_status);
						}
						?>
					</select>
				</div>

				<div class="form-row">
					<a class="anchor" name="billing_zip_code"><label for="billing_zip_code">Zip Code</label></a>
					<input type="text" data-nocounter="true" data-maxchar="20" name="billing_zip_code" id="billing_zip_code" value="<?php echo $order->getBillingZipCode() ?>" />
				</div>
			</div>
		</div>

		<div class="column short" style="width:250px">
			<div id="credit-card-info-wrap">
				<h2 class="heading clear credit-cards">Payment Information</h2>

				<img src="/img/cards.gif" height="28" alt="Credit Card Logos" />

				<a href="#" class="paypal-button"><img src="/img/checkoutwithpaypal.png" alt="Checkout with PayPal" /></a>

				<div class="form-row">
					<a class="anchor" name="payment_gateway"><label for="payment_gateway">Method</label></a>

					<select name="payment_gateway" id="payment_gateway">
						<option value="authorizenet">Credit Card</option>
						<option value="paypal">PayPal</option>
					</select>
				</div>

				<?php if (fAuthorization::checkLoggedIn() && count($paymentProfiles) > 0) : ?>
					<div class="form-row" data-gateway="authorizenet">
						<a class="anchor" name="payment_profile"><label for="payment_profile">Saved Card</label></a>
						<select name="payment_profile" id="payment_profile" required>
							<option value="">(New Card)</option>
							<?php
							foreach ($paymentProfiles as $paymentProfile) {
								echo sprintf('<option value="%s">%s - %s</option>' . PHP_EOL, $paymentProfile->getId(), $paymentProfile->getCardType(), $paymentProfile->getLast4());
							}
							?>
						</select>
					</div>
				<?php endif; ?>

				<div id="newCard">
					<div class="form-row" data-gateway="paypal-rest">
						<a class="anchor" name="credit_card_type"><label for="credit_card_type">Card Type</label></a>

						<select name="credit_card_type" id="credit_card_type">
							<option value="visa">Visa</option>
							<option value="mastercard">MasterCard</option>
							<option value="discover">Discover</option>
							<option value="amex">AmEx</option>
						</select>
					</div>

					<div class="form-row" data-gateway="authorizenet">
						<a class="anchor" name="credit_card_number"><label for="credit_card_number">Card Number</label></a>
						<input type="text" data-nocounter="true" data-maxchar="16" name="credit_card_number" id="credit_card_number" required value="" />
					</div>

					<div class="form-row" data-gateway="authorizenet">
						<a class="anchor" name="cc_ex_month"><label for="cc_ex_month">Exp Month</label></a>
						<select id="cc_ex_month" name="cc_ex_month" required>
							<?php
							for ($i = 01; $i < 13; $i++) {
								if ($i < 10) {
									$i = "0" . $i;
								}

								fHTML::printOption($i, $i);
							}
							?>
						</select>
					</div>

					<div class="form-row" data-gateway="authorizenet">
						<a class="anchor" name="cc_ex_year"><label for="cc_ex_year">Exp Year</label></a>

						<select id="cc_ex_year" name="cc_ex_year" required>
							<?php
							for ($i = date("Y"); $i < date("Y") + 20; $i++) {
								fHTML::printOption($i, $i);
							}
							?>
						</select>

						<?php if ( ($order->getTotal() > 0) && fAuthorization::checkLoggedIn() ) : ?>
							<div data-gateway="authorizenet" class="myauthorizenet">
								<br /><input style="margin-left: 90px;" type="checkbox" id="save_billing" name="save_billing" value="1" /><label style="float:initial" for="save_billing">Save for future use</label>
							</div>
						<?php endif; ?>
					</div>
				</div>

				<?php if ($order->getTotal() > 0) : ?>
					<div class="form-row">
						<p></p><p></p>
					</div>
				<?php endif; ?>

				<?php
				// coupon display
				$showCoupon = FALSE;
				if ( ($order->isNormalOrder() || $order->isCreditOnly()) && !$package->getNoDiscount() ) {
					$showCoupon = TRUE;
				}
				if ($showCoupon) {
					?>
					<div class="form-row">
						<label for="coupon">Coupon</label>
						<input type="text" data-nocounter="true" data-maxchar="20" id="coupon" name="coupon" value="<?php echo $return['coupon-name'] ?>" />
						<label for="apply_coupon">&nbsp;</label><input type="button" name="apply_coupon" id="apply_coupon" value="Apply Coupon" />
					</div>
					<?php
				}
				?>
			</div>
		</div>
	<?php } ?>

	<div class="clear completeOrder" style="width: 600px; float: left">
		<?php if ( $order->isPackageOrder() && $package->getNonprofit() ) : ?>
			<p class="note"><em>Note:</em> All nonprofits must be recognized by GuideStar and be the named source of the press release.</p>
		<?php endif; ?>

                <?php if ($orderType != 'misc-sale') : ?>
		<p class="total">Final Price: <span class="total" id="finalPrice"><?php echo money_format('%.2n', $order->getTotal());?></span><?php if ($order->getClientCreditsId() != NULL && fSession::get('skip_pressrelease_upload',NULL) == NULL) echo ' (after ' . $order->getPackageName() . ' Credit)'; ?> <span id="couponText"><?php echo $return['coupon']; ?></span></p>
                <?php endif; ?>

		<input type="hidden" name="writing" id="writing" value="<?php echo $order->getWriting(); ?>" />

		<div class="form-chech"><a name="agree_to_terms"><input type="checkbox" name="agree_to_terms" id="agree_to_terms" required /></a>&nbsp;&nbsp;<label class="my-label text" for="agree_to_terms">I agree to the <a target="_blank" href="http://www.ereleases.com/terms.html" />terms &amp; conditions</a></label></div>

		<p><label for="comments">Comments / Special Instructions:</label><br /><textarea rows="6" cols="70" name="comments" id="comments" style="width: 100%" <?php echo ($order->isMiscSale() ? 'required' : ''); ?>><?php echo $order->getComments(); ?></textarea></p>

		<p><input type="submit" name="check_out" class="greenBtn" value="Process my order!"  style="height: 48px;width: 101%;font-size: 24px;text-shadow: 2px 2px 0px #000;" /></p>

		<p class="note">If the newswire rejects your release, no charges will be incurred and you will be notified that the press release order has been cancelled.</p>
	</div>

	<div id="preview" class="column-alt short" style="">
		<h2>Order Details</h2>

		<table style="margin-top: 0px">
			<?php if ( $order->isCreditExtension() ) : ?>
				<tr>
					<td><strong>Order Type: </strong></td>
					<td>Credit Extension</td>
				</tr>

				<tr>
					<td><strong>Credit Extension Price: </strong></td>
					<td><?php echo money_format( '%.2n', $credit_extension->getPrice() ); ?></td>
				</tr>

				<tr>
					<td><strong>Extension Period: </strong></td>
					<td><?php echo $credit_extension->getExpirationMonths() ?> months</td>
				</tr>

				<tr>
					<td><strong>Package Name: </strong></td>
					<td><?php echo $package->getName(); ?></td>
				</tr>

				<tr>
					<td><strong>Old Credit Expiration Date: </strong></td>
					<td><?php echo $credit_old_expiration_date; ?></td>
				</tr>

				<tr>
					<td><strong>New Credit Expiration Date: </strong></td>
					<td><?php echo $credit_new_expiration_date; ?></td>
				</tr>
			<?php elseif ( $order->isMiscSale() ) : ?>
				<tr>
					<td><strong>Order Type: </strong></td>
					<td>Miscellanous Sale</td>
				</tr>

				<tr>
					<td><strong>Payment Amount: </strong></td>
					<td id="order_details_misc_payment_amount"><?php echo $order->getTotal(); ?></td>
				</tr>
			<?php else : ?>
				<tr>
					<td><strong>Service: </strong></td>
					<?php
					$packageName = $order->getPackageName();
					if ( $order->getWriting() ) {
						$packageName .= ' w/ Writing';
					}
					?>
					<td><?php echo $packageName; ?></td>
				</tr>

				<tr>
					<td><strong>Quantity:</strong></td>
					<td class="quantity-field"><?php echo $quantity ?></td>
				</tr>

				<?php if (!$order->isCreditOnly()) : ?>
					<tr>
						<td><strong>Distribution Date:&nbsp;&nbsp;&nbsp;</strong></td>
						<td><?php echo $order->niceDistributionDate(); ?></td>
					</tr>

					<?php if (!$order->getWriting()) { ?>
						<tr>
							<td><strong>Word Count: </strong></td>
							<td><?php echo ($order->getWordCount() > 0)? $order->getWordCount(): 'N/A'; ?></td>
						</tr>

						<tr>
							<td><strong>File Name: </strong></td>
							<td><?php echo $order->getReleaseContents(); ?></td>
						</tr>
					<?php } ?>

					<tr>
						<td><strong>No. of images uploaded: </strong></td>
						<td><?php echo ($order->getImageCount() > 0)? $order->getImageCount(): 'None'; ?></td>
					</tr>

					<tr>
						<td><strong>Industry Targets: </strong></td>
						<td><?php echo $order->getCategoryList(); ?></td>
					</tr>

					<tr>
						<td><strong>Local Area Saturation: </strong></td>
						<td>
							<?php
							if (!_empty($order->getLocalAreaSaturation())) {
								echo $order->getLocalAreaSaturation();
							} else {
								echo 'None';
							}
							?>
						</td>
					</tr>

					<tr>
						<td><strong>Influencers Selected: </strong></td>
						<td>
							<?php
							if (!_empty($order->getInfluencers())) {
								$influencers = $order->getInfluencers();
								?>
								<ul>
									<?php foreach ($influencers AS $influencer) : ?>
										<li><?php echo $influencer; ?></li>
									<?php endforeach; ?>
								</ul>
								<?php
							} else {
								echo 'None';
							}
							?>
						</td>
					</tr>

					<tr>
						<td><strong>International: </strong></td>
						<td>
							<?php
							if ($order->countCountries() > 0) {
								$countries = $order->getCountries();
								?>
								<ul>
									<?php foreach ($countries AS $country) : ?>
										<li><?php echo $country; ?></li>
									<?php endforeach; ?>
								</ul>
								<?php
							} else {
								?>None<?php
							}
							?>
						</td>
					</tr>
				<?php endif; ?>

				<tr>
					<td><strong>Video: </strong></td>
					<td><?php echo ($order->getEmbedVideo()) ? 'Yes' : 'No'; ?></td>
				</tr>

				<tr>
					<td><strong>Price: </strong></td>
					<td><span id="finalPriceSide"><?php echo money_format('%.2n', $order->getTotal());?></span><?php if ($order->getClientCreditsId() != NULL && fSession::get('skip_pressrelease_upload',NULL) == NULL) echo ' (after Credit)'; ?></td>
				</tr>

				<tr>
					<td><strong>Breakdown:</strong></td>
					<td>
						<?php
						$bd = $order->getBreakdownItems();
						$j = ($order->getWriting()) ? 2 : 1;
						if (!$bd) {
							?><h5 style="margin: 10px; margin-bottom: 0; font-weight: normal;">unavailable</h5><?php
						} else {
							?>
							<table>
								<tbody>
									<?php for ($i = 0; $i < count($bd); $i++) : ?>
										<tr>
											<td><?php echo $bd[$i]['name'] ?></td>
											<td <?php if ($i<$j) echo 'class="quantity-field"' ?>><?php echo $bd[$i]['quantity'] ?></td>
											<td <?php
											if ($i<$j) {
												if ($i==1) {
													echo 'class="wprice-field"';
												} else {
													echo 'class="price-field"';
												}
											}
											?>><?php
												$bdItemAmount = $bd[$i]['amount'] ? doubleval( $bd[$i]['amount'] ) : 0.00;

												echo money_format('%.2n', $bdItemAmount );
											?></td>
										</tr>
									<?php endfor; ?>
								</tbody>
							</table>
							<?php
						}
						?>
					</td>
				</tr>
			<?php endif; // if ( $order->isCreditExtension() ) ?>
		</table>
	</div>
</form>

<script type="text/javascript">
	// this was added only for the Logging feature. It wasn't here before. -AQ
	var orderId = <?php echo ($orderId) ? $orderId : $order->getId() ?>;

	$(document).ready(function() {
		$("input:hidden,select:hidden").removeAttr('required');

		if ($('#payment_profile').val() == "") {
			$('#payment_profile').removeAttr('required')
			$('input#credit_card_number').attr('required', 'required')
		} else {
			$('#payment_profile').attr('required', 'required')
			$('input#credit_card_number').removeAttr('required')
		}

		$('#order').submit(function() {
			// warning: this is not the proper way to check if a checkbox is checked.
			// proper way is to check the 'checked' property.
			if (!$('#agree_to_terms', this).is(':checked')) {
				Logger.write('Form submitting without agreeing to terms', '<?php echo __FILE__ ?>', <?php echo __LINE__ ?>, orderId);
				alert('You must agree to the terms and conditions!');
				return false;
			}
			Logger.write('Form submitted without client side errors', '<?php echo __FILE__ ?>', <?php echo __LINE__ ?>, orderId);
		});

		$('select#billing_state').change(function() {
			if ($('select#billing_state').val() == 'Other') {
				$('input#billing_state_other').show().prev().show();
			} else {
				$('input#billing_state_other').hide().prev().hide();
			}
		});

//		$('input[name="package_price_id"]').change(updatePrice);
//		$('input[name="coupon"]').change(updatePrice);
//		$('#apply_coupon').click(updatePrice);

		// Misc Sale
		$('#misc_sale_payment_amount').change(function () {
			var $amountField = $(this);
			var priceText = '$' + $amountField.val();

			$('#finalPrice').text(priceText);
			$('#order_details_misc_payment_amount').text(priceText);
		});
		$('#misc_sale_payment_amount').trigger('change');

        updatePrice();
	});

	$('.radio-upgrade').change(function() {
		var $this = $(this);
		if ($this.prop('checked')) {
            var credits = $this.attr('data-credits');
			$('.quantity-field').text($this.attr('data-credits'));
			$('.price-field').text($this.attr('data-price'));
			$('.wprice-field').text('$' + (parseInt($this.attr('data-wprice')) * parseInt($this.attr('data-credits'))) + '.00');
            $('.radio-upgrade').each(function() {
                var $$this = $(this);
                var $label = $('label[for=' + $$this.val() + ']');
                if (credits == parseInt($$this.attr('data-credits'))) {
                    console.log(credits + ' < ' + $$this.attr('data-credits'));
                    $label
                            .css('font-weight', 'bold')
                            .find('span.pkgVerbage').text('You have selected');
                } else if (credits <= parseInt($$this.attr('data-credits'))) {
                    console.log(credits + ' < ' + $$this.attr('data-credits'));
                    $label
                            .css('font-weight', '')
                            .find('span.pkgVerbage').text('Upgrade to');
                } else {
                    console.log(credits + ' > ' + $$this.attr('data-credits'));
                    $label
                            .css('font-weight', '')
                            .find('span.pkgVerbage').text('Downgrade to');
                }
            });
    	}
    });

	// we want to log changes to all input elements that aren't checkboxes (checkboxes handled separately)
	// and also textareas.
	$('input:not(:checkbox), textarea, select').change(function(e) {
		var eName = $(e.target).attr('name');
		var eValue = $(e.target).val();
		// we don't want to store the person's credit card number in the log, so we replace it with *'s except for the last 4 digits
		if (eName == 'credit_card_number') {
			eValue = eValue.replace(/.*(.{4})/, "************$1");
		}
		Logger.write('Form field "' + eName + '" changed to: ' + eValue, '<?php echo __FILE__ ?>', <?php echo __LINE__ ?>, orderId);
                updatePrice();
	});

	// we have to treat checkboxes differently
	$(':checkbox').change(function(e) {
		var eName = $(e.target).attr('name');
		var checked = $(this).prop('checked');
		if (checked) {
			Logger.write('Checkbox "' + eName + '" checked', '<?php echo __FILE__ ?>', <?php echo __LINE__ ?>, orderId);
		}	else {
			Logger.write('Checkbox "' + eName + '" unchecked', '<?php echo __FILE__ ?>', <?php echo __LINE__ ?>, orderId);
		}
                updatePrice();
	});

	$('#billing_same').on('click', function(e) {
		if ($('#billing_same').prop('checked')) {
			Logger.write('User checked billing same checkbox. Copying information', '<?php echo __FILE__ ?>', <?php echo __LINE__ ?>, orderId);
			$('#billing_first_name').val($('#first_name').val());
			$('#billing_last_name').val($('#last_name').val());
			$('#billing_company').val($('#company').val());
			$('#billing_address').val($('#address').val());
			$('#billing_address_2').val($('#address_2').val());
			$('#billing_city').val($('#city').val());
			$('#billing_state').val($('#state').val());
			$('#billing_country').val($('#country').val());
			$('#billing_zip_code').val($('#zip_code').val());
		}
	});

	// trim whitespace from coupon
	$('#coupon').change(function() {
		var $this = $(this);
		$this.val($this.val().trim());
	});

	$('#payment_profile').change(function(e) {
		if ($('#payment_profile').val() > 0) {
			$('div#newCard').hide();
			$('#payment_profile').attr('required', 'required')
			$('input#credit_card_number').removeAttr('required')
		} else {
			$('div#newCard').show();
			$('#payment_profile').removeAttr('required')
			$('input#credit_card_number').attr('required', 'required')
		}
	});

	function updatePrice() {
		$.post("/price.php", $('#order').serialize(), function(data) {
			$('#finalPrice').html(data.price);
			$('#finalPriceSide').html(data.price);
			if (data.coupon && data.coupon.length > 0) {
				$('#couponText').html('(' + data.coupon + ')');
			} else {
				$('#couponText').html(data.coupon);
			}

		}, 'json');
	}

	function updateCCFields() {
		var gateway = $('#payment_gateway').val();
		$('#credit-card-info-wrap *[data-gateway]').hide().filter('*[data-gateway="' + gateway + '"]').show();
		$("input:hidden,select:hidden").removeAttr('required');
	}

	$(document).ready(function(){
		$('#payment_gateway').change(updateCCFields).trigger('change');
		$('.paypal-button').on('click', function(e) {
			e.preventDefault();
			$('#payment_gateway').val('paypal').trigger('change');
		});
	});

    history.pushState(null, document.title, location.href);
    history.back();
    history.forward();
    window.onpopstate = function () {
        history.go(1);
    };
</script>
