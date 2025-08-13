<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = isset($_POST['name']) ? trim($_POST['name']) : '';
    $email = isset($_POST['email']) ? trim($_POST['email']) : '';
    $subject = isset($_POST['subject']) ? trim($_POST['subject']) : '';
    $message = isset($_POST['message']) ? trim($_POST['message']) : '';
    
    // Basic validation
    if (empty($name) || empty($email) || empty($subject) || empty($message)) {
        echo "تمام خانے پُر کرنا ضروری ہے";
        exit;
    }
    
    // Email validation
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "صحیح ای میل ایڈریس درج کریں";
        exit;
    }
    
    // Sanitize input
    $name = htmlspecialchars($name);
    $email = htmlspecialchars($email);
    $subject = htmlspecialchars($subject);
    $message = htmlspecialchars($message);
    
    // Email configuration
    $to = "info@virtualislamicuniversity.com";
    $email_subject = "Contact Form: " . $subject;
    $email_body = "Name: $name\n";
    $email_body .= "Email: $email\n\n";
    $email_body .= "Message:\n$message";
    
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    
    // Send email
    if (mail($to, $email_subject, $email_body, $headers)) {
        echo "OK";
    } else {
        echo "پیغام بھیجنے میں خرابی ہوئی، براہ کرم دوبارہ کوشش کریں";
    }
} else {
    echo "Invalid request method";
}
?>
