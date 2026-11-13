# IshanGPT

## Configure the question form

1. Create a form in Formspree and verify the inbox that should receive questions.
2. Set the form ID as `FORMSPREE_FORM_ID` in the app environment.
   - On Vercel, add it under **Project Settings → Environment Variables**, then redeploy.
   - Locally, run the app with `FORMSPREE_FORM_ID=<your-form-id>` set in the environment.

The form posts directly from the browser to Formspree, so no email API key or custom sending domain is needed. The form ID is public; do not put a private API key in the HTML.
