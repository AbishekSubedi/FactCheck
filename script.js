async function handleSubmit() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    
    // Add user message
    chatBox.innerHTML += `
        <div class="message user-message">
            ${input.value}
        </div>
    `;
    
    // Add loading indicator
    chatBox.innerHTML += `
        <div class="message bot-message loading">
            Analyzing...
        </div>
    `;
    
    try {
        const response = await fetch('https://factcheck-cfib.onrender.com/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input: input.value })
        });
        
        const data = await response.json();
        console.log("Backend response:", data);  // Log backend response
        
        // Remove loading indicator
        chatBox.querySelector('.loading').remove();
        
        // Add bot response
        chatBox.innerHTML += `
            <div class="message bot-message">
                <h3>Analysis Results:</h3>
                <p>🔍 Fake News Detection: ${data.fake_news.verdict} (${data.fake_news.confidence}% confidence)</p>
                <p>📝 Reasons: ${data.fake_news.reasons.join(", ")}</p>
                <p>🤖 AI-Generated: ${data.ai_generated.is_ai ? 'Yes' : 'No'} (${data.ai_generated.confidence}%)</p>
                <p>🧠 Sentiment: ${data.sentiment.sentiment} (Score: ${data.sentiment.polarity_score})</p>
                ${data.fact_check ? `<p>✅ Fact Check: ${data.fact_check}</p>` : ''}
            </div>
        `;
        
    } catch (error) {
        console.error('Error:', error);  // Log fetch errors
        chatBox.querySelector('.loading').remove();
        chatBox.innerHTML += `
            <div class="message bot-message">
                Error: Could not analyze the content
            </div>
        `;
    }
    
    input.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
}
