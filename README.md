 <h1> SurBot </h1>
 
  <strong>SurBot</strong> - IRC Bancho bot for osu! Project is under development, new feautures soon!
  
  <h2>How to use?</h2>
    In game press F8 to open chat. Then write /chat SuRory. Now you can use use commands:
    
   <i>*There are arguments in []. = means default value</i>
  <ul>
  <li>.pp [mods=nomod, acc=95, 100, miss=0, 0, combo=max] - display pps for map in /np with specific parametrs. If you don't want to use arguments, just use .pp without anything else.
  
  When you wrote /np you can use .pp:
  
  ![](blob/no_args.png?raw=true)
  
  You can use keyword and non-keyword arguments.
  <strong><i>You can use only 1 value for miss or acc. 95, 100 and 0, 0 means that your parameter adds to those</i></strong>
  
  It's possible to combine keyword args and non-keyword args. Just use keyword args after right-ordered non-keyword args:
  
  ![](blob/args.png?raw=true)
  
  </li>
  <li>.pp_pred [mods=nomod, acc=95, 100, miss=0, 0, combo=max] - actually same as .pp but with predicted pps based on player's scores
 </li>
 
  <li>.info - displays information about commands.
  </li>
  </ul>
  
  <h2>How to install?</h2>
  You can clone all the code and use bot on your own account!
  Simple steps:
  <ul>
  <li>Install Python 3.6 or higher</li>
  <li>Clone code from repository</li>
  <li>Run main.py</li>
  <li>If you want to connect in some channels, use bot.connect(channel) for every channel you want to join.</li>
  <li>Use bot.run() to run bot. Done!</li>
  </ul>
