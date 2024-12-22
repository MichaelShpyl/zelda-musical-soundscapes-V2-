package test;

// Importing the main MusicPlayer class to test it out.
import main.MusicPlayer;
// JUnit stuff for testing. Gotta make sure things actually work!
import org.junit.Test;
import static org.junit.Assert.assertEquals;

// Okay, now we're testing if the MusicPlayer actually works.
public class MusicPlayerTest {

    // This is where we test if the playSound method does its thing.
    @Test
    public void testPlaySound() {
        // Creating a MusicPlayer object.
        MusicPlayer player = new MusicPlayer();
        
        // Playing a sound (well, just printing it for now).
        player.playSound("zelda-theme"); // "Zelda-theme" is the test sound. Classic!
        
        // We're not really checking anything here, just running it to see if it prints correctly.
        // Could improve this later, maybe mock the output?
    }
}
