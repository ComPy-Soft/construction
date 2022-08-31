def pages(request):
    Registration = {
    "all_registration_pages": [
        "add_customers",
        "manage_customers",
        "add_vendor",
        "manage_vendor",
        "add_estate_agents",
        "manage_estate_agents",
        "add_product_types",
        "manage_product_types",
        "add_products",
        "manage_products",
        "add_taxes",
        "manage_taxes",
        "add_bank_accounts",
        "manage_bank_accounts",
        "add_assets",
        "manage_assets",
        "add_users",
        "manage_users",
        "add_expense_types",
        "manage_expense_types",
        "add_warehouses",
        "manage_warehouses",
    ],
    "customers": [
        "add_customers",
        "manage_customers"
    ],
    "vendor": [
        "add_vendor",
        "manage_vendor"
    ],
    "estateAgents": [
        "add_estate_agents",
        "manage_estate_agents"
    ],
    "producttypes": [
        "add_product_types",
        "manage_product_types"
    ],
    "products": [
        "add_products",
        "manage_products"
    ],
    "taxes": [
        "add_taxes",
        "manage_taxes"
    ],
    "bankacounts": [
        "add_bank_accounts",
        "manage_bank_accounts"
    ],
    "assets": [
        "add_assets",
        "manage_assets"
    ],
    "users": [
        "add_users",
        "manage_users"
    ],
    "expensetypes": [
        "add_expense_types",
        "manage_expense_types"
    ],
    "warehouses": [
        "add_warehouses",
        "manage_warehouses"
    ],
    "all_account_pages": [
        "add_bank_deposit_voucher",
        "add_debit_notes",
        "add_expense_voucher",
        "add_journal_voucher",
        "add_opening_voucher",
        "add_payment_voucher",
        "add_receipt_voucher",
        "chart_of_accounts",
        "manage_bank_deposit_voucher",
        "manage_debit_notes",
        "manage_expense_voucher",
        "manage_journal_voucher",
        "manage_opening_voucher",
        "manage_payment_voucher",
        "manage_receipt_voucher",
    ],
    "PaymentVouchers": [
        "manage_payment_voucher",
        "add_payment_voucher"
    ],
    "ExpenseVouchers": [
        "add_expense_voucher",
        "manage_expense_voucher"
    ],
    "ReceiptVouchers": [
        "add_receipt_voucher",
        "manage_receipt_voucher"
    ],
    "OpeningVouchers": [
        "add_opening_voucher",
        "manage_opening_voucher"
    ],
    "JournelVouchers": [
        "add_journal_voucher",
        "manage_journal_voucher"
    ],
    "DebitNotes": [
        "add_debit_notes",
        "manage_debit_notes"
    ],
    "BankDeposits": [
        "add_bank_deposit_voucher",
        "manage_bank_deposit_voucher"
    ],
    "ChartOfAccounts": [
        "chart_of_accounts"
    ],

    "all_sales_pages":[
        "add_additional_charges",
        "manage_additional_charges",
        "add_agent_commission",
        "manage_agent_commission",
        "add_property_buy_back",
        "manage_property_buy_back",
        "add_installment_plan",
        "manage_installment_plan",
        "add_installment_plan_B",
        "manage_installment_plan_B",
        "generate_properties",
        "manage_properties",
        "add_property_cancellation",
        "manage_property_cancellation",
        "add_property_transfer",
        "manage_property_transfer",
        "add_property_merger",
        "manage_property_merger",
        "add_property_sale",
        "manage_property_sale",
        "add_property_surcharge",
        "manage_property_surcharge",
        "add_surcharge_waiver",
        "manage_surcharge_waiver",
        "master_delete_property_sales",
        "upgrade_property_prices"
    ],
    "additionalcharges": [
        "add_additional_charges",
        "manage_additional_charges"
    ],
    "agentcommission": [
        "add_agent_commission",
        "manage_agent_commission"
    ],
    "propertybuyback": [
        "add_property_buy_back",
        "manage_property_buy_back"
    ],
    "installmentplan": [
        "add_installment_plan",
        "manage_installment_plan"
    ],
    "installmentplanB": [
        "add_installment_plan_B",
        "manage_installment_plan_B"
    ],
    "generateproperties": [
        "generate_properties",
        "manage_properties"
    ],
    "propertycancellation": [
        "add_property_cancellation",
        "manage_property_cancellation"
    ],
    "propertytransfer": [
        "add_property_transfer",
        "manage_property_transfer"
    ],
    "propertymerger": [
        "add_property_merger",
        "manage_property_merger"
    ],
    "propertysale": [
        "add_property_sale",
        "manage_property_sale"
    ],
    "propertysurcharge": [
        "add_property_surcharge",
        "manage_property_surcharge"
    ],
    "surchargewaiver": [
        "add_surcharge_waiver",
        "manage_surcharge_waiver"
    ],
    "deletepropertysales": [
        "master_delete_property_sales",
    ],
    "upgradepropertyprices": [
        "upgrade_property_prices"
    ],
    "all_construction_pages":[
        "add_construction_note",
        "construction_stage_chart",
        "manage_construction_note"
    ],
    "constructionnotes": [
        "add_construction_note",
        "manage_construction_note"
    ],
    "constructionstagechart": [
        "construction_stage_chart"
    ]
}
    return {"pages": Registration}
