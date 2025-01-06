---
title: Adding Auto Classification Workflow through UI
slug: /how-to-guides/data-governance/classification/auto/workflow
---

# Adding Auto Classification Ingestion through the UI

Follow these steps to configure Auto Classification ingestion via the OpenMetadata UI:

## 1. Navigate to the Database Service
- Go to **Settings > Services > Databases** in the OpenMetadata UI.
- Select the database for which you want to configure Auto Classification ingestion.

{% image
src="/images/v1.7/how-to-guides/governance/ac-1.png"
alt="Settings"
caption="Settings"
/%}

{% image
src="/images/v1.7/how-to-guides/governance/ac-1.1.png"
alt="Services"
caption="Services"
/%}

{% image
src="/images/v1.7/how-to-guides/governance/ac-2.png"
alt="Databases"
caption="Databases"
/%}

## 2. Access the Ingestion Tab
- In the selected database, navigate to the **Ingestion** tab.
- Click on the option to **Add Auto Classification Ingestion**, as shown in the example image.

{% image
src="/images/v1.7/how-to-guides/governance/ac-3.png"
alt="Access the Ingestion Tab"
caption="Access the Ingestion Tab"
/%}

## 3. Configure Auto Classification Details
- Fill in the details for your Auto Classification ingestion workflow.
- Each field's purpose is explained directly in the UI, allowing you to customize the configuration based on your requirements.

{% image
src="/images/v1.7/how-to-guides/governance/ac-4.png"
alt="Configure Auto Classification Details"
caption="Configure Auto Classification Details"
/%}

## 4. Set the Schedule
- Specify the time interval at which the Auto Classification ingestion should run.

{% image
src="/images/v1.7/how-to-guides/governance/ac-5.png"
alt="Set the Schedule"
caption="Set the Schedule"
/%}

## 5. Add the Ingestion Workflow
- Once all details are configured, click **Add Auto Classification Ingestion** to save and activate the workflow.

{% image
src="/images/v1.7/how-to-guides/governance/ac-6.png"
alt="Add the Ingestion Workflow"
caption="Add the Ingestion Workflow"
/%}

By following these steps, you can set up an Auto Classification ingestion workflow to automatically identify and tag sensitive data in your databases.