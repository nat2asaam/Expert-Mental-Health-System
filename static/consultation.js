function titleCase(s) {
    try{
        return s.toLowerCase()
                .split(' ')
                .map(word => word.charAt(0).toUpperCase() + word.slice(1))
                .join(' ');
    } catch (error) {
        window.console && console.error('Error in titleCase function:', error);
        return s; // Return the original string if there's an error
    }
}
$(document).ready(function() {
    window.console && console.log('Consultation page loaded');
    var analysisResult="";
    $("#analyze-btn").click(function() {
        window.console && console.log('Analyze button clicked');
        var text = $('#text-to-analyze').val();
        window.console && console.log('Text to analyze:', text);
         $.ajax({
            url: '/analyze-text',
            type: 'POST',
            data: { text: text },
            success: function(response) {
                window.console && console.log(response);
                analysisResult=response;
                // Handle the analysis results
                $('#keyword1').text('');
                $('#emotion1').text('');
                $('#sentiment1').text('');
                $('#keyword2').text('');
                $('#emotion2').text('');
                $('#sentiment2').text('');
                $('.analysis-results').hide();
                var keywords = response.keywords;
                keyword1=keywords[0] || 'N/A';
                keyword2=keywords[1] || 'N/A';
                if(keyword1=='N/A'){
                    $('#keyword1').text('N/A');
                    $('#sentiment1').text('N/A').removeClass('text-success text-warning');
                    $('#emotion1').text('N/A');
                    return;
                }
                $('#keyword1').text(titleCase(keyword1.text));
                $('#sentiment1').text(titleCase(keyword1.sentiment.label));
                if(keyword1.sentiment.label=='positive'){
                    $('#sentiment1').removeClass('text-warning').addClass('text-success');
                } else if(keyword1.sentiment.label=='negative'){
                    $('#sentiment1').removeClass('text-success').addClass('text-warning');
                }
                 else{
                    $('#sentiment1').removeClass('text-success text-warning');
                }
                var emotion1=keyword1.emotion || 'N/A';
                var emotion1Label="Anger";
                currentEmotionValue=emotion1.anger || 0;
                if(currentEmotionValue<emotion1.joy){
                    emotion1Label="Joy";
                    currentEmotionValue=emotion1.joy;
                }
                if(currentEmotionValue<emotion1.fear){
                    emotion1Label="Fear";
                    currentEmotionValue=emotion1.fear;
                }
                if(currentEmotionValue<emotion1.sadness){
                    emotion1Label="Sadness";
                    currentEmotionValue=emotion1.sadness;
                }
                if(currentEmotionValue<emotion1.disgust){
                    emotion1Label="Disgust";
                    currentEmotionValue=emotion1.disgust;
                }
                $('#emotion1').text(titleCase(emotion1Label));
                if(emotion1Label=='Joy'){
                    $('#emotion1').removeClass('text-danger').addClass('text-info');
                }
                else{
                    $('#emotion1').removeClass('text-info').addClass('text-danger');
                }
                if(keyword2=='N/A'){
                    $('#keyword2').text('N/A');
                    $('#sentiment2').text('N/A').removeClass('text-success text-warning'); 
                    $('#emotion2').text('N/A');
                }    
                $('#keyword2').text(titleCase(keyword2.text));
                $('#sentiment2').text(titleCase(keyword2.sentiment.label));
                if(keyword2.sentiment.label=='positive'){
                    $('#sentiment2').removeClass('text-warning').addClass('text-success');
                } else if(keyword2.sentiment.label=='negative'){
                    $('#sentiment2').removeClass('text-success').addClass('text-warning');
                }
                else{
                    $('#sentiment2').removeClass('text-success text-warning');
                }
                var emotion2=keyword2.emotion || 'N/A';
                var emotion2Label="Anger";
                var currentEmotionValue2=emotion2.anger;
                if(currentEmotionValue2<emotion2.joy){
                    emotion2Label="Joy";
                    currentEmotionValue2=emotion2.joy;
                }
                if(currentEmotionValue2<emotion2.fear){
                    emotion2Label="Fear";
                    currentEmotionValue2=emotion2.fear;
                }
                if(currentEmotionValue2<emotion2.sadness){
                    emotion2Label="Sadness";
                    currentEmotionValue2=emotion2.sadness;
                }
                if(currentEmotionValue2<emotion2.disgust){
                    emotion2Label="Disgust";
                    currentEmotionValue2=emotion2.disgust;
                }
                $('#emotion2').text(titleCase(emotion2Label));
                if(emotion2Label=='Joy'){
                    $('#emotion2').removeClass('text-danger').addClass('text-info');
                }
                else{
                    $('#emotion2').removeClass('text-info').addClass('text-danger');
                }
                //$('.analysis-results').show();
                $('.analysis-results').slideDown(800,'swing',function(){console.log('EOF');});
            },
            error: function(xhr, status, error) {
                    window.console && console.error('Error:', error);
                    alert('An error occurred while analyzing the text. You text did not return any results. Please try again.');
            }
        });
    }); 
});