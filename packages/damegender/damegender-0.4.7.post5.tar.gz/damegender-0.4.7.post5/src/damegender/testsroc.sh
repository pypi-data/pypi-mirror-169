if [ -f files/names/names_test/allnoundefined.csv ]; then
    python3 roc.py gaussianNB --noshow
    if [ -f files/images/roc_gaussianNB.png ]; then
	echo -e  "roc test is ${GREEN}ok${NC}"
    else
	echo -e  "roc test is ${RED}failing${NC}"
    fi
fi
