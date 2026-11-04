## How to set up the environment

1. Open your terminal and navigate to the root directory containing the `pyproject.toml` file.
2. Run the sync command:
   ```bash
   uv sync
   ```
   It checks the `pyproject.toml` file, creates a virtual environment (`.venv`) if one does not exist, updates the `uv.lock` file, and installs all listed packages.
3. Navigate to the `notebooks` folder.
4. Rename the `.env_copy` file to `.env` and add your API keys for OpenAI, Gemini, and any other services you plan to use.

## Steps to obtain API keys

**Groq API key:**

1. Go to [console.groq.com](https://console.groq.com) and sign up (email, Google, or GitHub).
2. Click the hamburger menu → **API Keys** (or go directly to [console.groq.com/keys](https://console.groq.com/keys)).
3. Click **Create API Key**, give it a name, and copy the key immediately — it starts with `gsk_` and is shown only once.

---

**Google (Gemini AI Studio) API Key:**

  * Go to [Google AI Studio](https://aistudio.google.com/).
  * Sign in with your Google account.
  * On the left-hand navigation menu, click on **API keys**.
  * Click the **Create API key** button present at the top right corner.
  * Select an existing Google Cloud project or create a new one, then generate and copy your `GOOGLE_API_KEY`.

---

**Supermemory API Key:**

  * Visit [Supermemory.ai](https://supermemory.ai/) and sign in or create an account.
  * Navigate to your dashboard or profile settings.
  * Locate the **API Keys** under _Developer_ section.
  * Click `Create Key` to generate a new API key and copy it for your notebook.

---

**Qdrant Cloud Credentials**

  1. Go to [Qdrant Cloud](https://cloud.qdrant.io/) and sign in using your email, Google account, or GitHub account.
  2. Open **Clusters** and select **Create a Free Cluster**, or click **+ Create** and choose the **Free** cluster option.
  3. Select an available cloud provider and a region close to your application or users, provide a cluster name, and create the cluster.
  4. When the cluster is ready, copy the **Cluster Endpoint** shown on the cluster page. Store it as:

      ```env
      QDRANT_URL=https://your-cluster-endpoint
      ```

  5. During cluster creation, Qdrant may display an initial API key. Copy and securely store it immediately because the key is shown only once. Store the key as:

      ```env
      QDRANT_API_KEY=your-qdrant-api-key
      ```

---

**Langfuse Cloud Credentials:**

  1. Open the Langfuse Cloud URL for the region in which you want your data to be stored:
      * **EU, Ireland:** `https://cloud.langfuse.com`
      * **US, Oregon:** `https://us.cloud.langfuse.com`
      * **Japan, Tokyo:** `https://jp.cloud.langfuse.com`

  2. Sign in or create an account in the selected region.
  3. Create a new Langfuse project for this session.

  4. When the project is created, Langfuse may generate project API credentials automatically. You can also view or create credentials by navigating to:  
      **Project → Settings → API Keys**

  5. Copy the generated credentials and store them as:

      ```env
      LANGFUSE_PUBLIC_KEY=pk-lf-...
      LANGFUSE_SECRET_KEY=sk-lf-...
      ```

  6. Configure the Langfuse base URL corresponding to the region in which the project was created:

      ```env
      # EU region
      LANGFUSE_BASE_URL=https://cloud.langfuse.com
      
      # US region
      LANGFUSE_BASE_URL=https://us.cloud.langfuse.com
      
      # Japan region
      LANGFUSE_BASE_URL=https://jp.cloud.langfuse.com
      ```
