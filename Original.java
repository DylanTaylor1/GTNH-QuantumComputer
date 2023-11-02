import java.util.List;
import java.util.ArrayList;

System.out.println("Test");

public class Main
{
    public static void main(String[] args)
    {
        Rack rack = new Rack(new ArrayList<>() {{
                    // 3 Crystalprocessor Mainframes and 1 Advanced Heat Vent as example
                    add(new Rack.RackComponent(18, -.35f));
                    add(new Rack.RackComponent(18, -.35f));
                    add(new Rack.RackComponent(18, -.35f));
                    add(new Rack.RackComponent(-1, 80f));
                }},
                // Overclock (=1 if not overclocked)
                1.0f,
                // Overvolt (=1 if not overvolted)
                1.0f
        );
        int oldHeat = 0, newHeat = 10000;
        while (Math.abs(newHeat - oldHeat) > 0)
        {
            oldHeat = newHeat;
            rack.getComputation();
            rack.onPostTick();
            newHeat = rack.heat;
        }

        System.out.println("Final heat approx: " + newHeat);
    }

    private static class Rack
    {
        public int heat = 0;
        List<RackComponent> components;
        float overclock = 1;
        float overvolt = 1;

        public Rack(List<RackComponent> components, float overclock, float overvolt)
        {
            this.components = components;
            this.overclock = overclock;
            this.overvolt = overvolt;
        }

        public void onPostTick()
        {
            if (heat > 0)
            {
                float heatC = 0f;

                for (RackComponent comp : components)
                {
                    if (comp.heat < 0) {
                        heatC += comp.heat * (heat / 10000f);
                    }

                    heat += Math.max(-heat, Math.ceil(heatC));
                }

                heat -= Math.max(heat / 1000, 1);
            }
            else if (heat < 0)
            {
                heat -= Math.min(heat / 1000, -1);
            }
        }

        public void getComputation()
        {
            float rackHeat = 0f;

            for (RackComponent comp : components)
            {
                if (heat >= 0)
                    rackHeat += (1f + comp.heatCoeff * heat / 10000f) * (comp.heat > 0 ? comp.heat * overvolt * overclock * overclock : comp.heat);
            }

            heat += Math.ceil(rackHeat);
        }

        private static class RackComponent
        {
            public int heat;
            public float heatCoeff;

            public RackComponent(int initialHeat, float heatCoeff)
            {
                heat = initialHeat;
                this.heatCoeff = heatCoeff;
            }
        }
    }
}